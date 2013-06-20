#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/20/13 08:33:23 (CST)
# Modified Time: 06/20/13 08:49:05 (CST)
import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Helllo World"
        return render.index(greeting= greeting)
if __name__ == "__main__":
    app.run()
