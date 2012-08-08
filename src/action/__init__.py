#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join
from depend.bottle import Bottle,static_file
from depend.bottle import debug, run
from depend.bottle import redirect, abort, static_file
from depend.bottle import jinja2_template as template
from depend.bottle import request, response, local
from depend.bottle import TEMPLATE_PATH
from conf.setting import CUSTOM_TPL_PATH
from conf.setting import STATIC_FILE_PATH
from conf.setting import IMAGES_FILE_PATH
from conf.setting import JS_FILE_PATH
TEMPLATE_PATH.insert(0, CUSTOM_TPL_PATH)
sys.path.insert(0, abspath(dirname(__file__)))
root = Bottle()

root.mount('/movie', __import__('movie').app)
root.mount('/login', __import__('login').app)
root.mount('/user', __import__('user').app)

@root.route('/static/<filename>')
def static(filename):
    return static_file(filename, root=STATIC_FILE_PATH)

@root.route('/images/<filename>')
def images(filename):
    return static_file(filename, root=IMAGES_FILE_PATH)

@root.route('/images/<path:path>')
def images(path):
    return static_file(path, root=IMAGES_FILE_PATH)

@root.route('/js/<filename>')
def js(filename):
    return static_file(filename, root=JS_FILE_PATH)

@root.route('/js/<path:path>')
def js(path):
    return static_file(path, root=JS_FILE_PATH)

@root.route('/center')
def handel_redirect():
    return redirect(request.path+'/')

@root.route('/')
def handle_index():
    return '我是首页'

if __name__ == '__main__':    
    debug(True)
    run(root, host="0.0.0.0",reloader=True)
