#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 07/18/13 18:22:06 (CST)
# Modified Time: 07/24/13 08:56:46 (CST)

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       # ex: /polls/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # ex: /polls/5/
                       #url(r'^(?P<poll_id>\d+)/$',views.detail, name='detail'),
                       url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
                       # ex: /polls/5/results/
                       url(r'^(?P<poll_id>\d+)/results/$',views.ResultsView.as_view(), name='results'),
                       # ex:/polls/5/vote/
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       )
