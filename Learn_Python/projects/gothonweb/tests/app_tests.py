#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/20/13 18:57:06 (CST)
# Modified Time: 06/21/13 08:54:08 (CST)
from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # test our first GET request to /hello URL
    resp = app.request("/hello")
    assert_response(resp)

    # make sure default values work from the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    # t est that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
