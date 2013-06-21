#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/20/13 08:33:23 (CST)
# Modified Time: 06/21/13 17:09:24 (CST)
import web
import map
urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

#render = web.template.render('templates/', base="layout")
# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})

    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        #this is used to "setup" the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # why is there here? do you need it?
            return render.you_died()


    def POST(self):
        form =  web.input(action=None)
        #ther is a bug here can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

        #greeting = "%s, %s" % (form.greet, form.name)
        #return render.index(greeting=greeting)

if __name__ == "__main__":
    app.run()
