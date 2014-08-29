#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os.path import abspath, dirname
from awspy.Utils.Utils import *
from depend.bottle import Bottle,get,post,debug,run,redirect,static_file,request,error,route
from depend.bottle import TEMPLATE_PATH
from conf.setting import CUSTOM_TPL_PATH
from conf.setting import STATIC_FILE_PATH
from conf.setting import IMAGES_FILE_PATH
from conf.setting import JS_FILE_PATH
from conf.setting import CSS_FILE_PATH
from conf.setting import UPLOAD_FILE_PATH
from depend.beaker.middleware import SessionMiddleware
TEMPLATE_PATH.insert(0, CUSTOM_TPL_PATH)
sys.path.insert(0, abspath(dirname(__file__)))


root = Bottle()




# listfile=os.listdir(dirname(__file__))
# listmount=[]
# for line in listfile:
#     tmp=line[:line.find('.')]
#     if listmount.count(tmp)==0:
#         if tmp!='__init__':
#             root.mount('/'+tmp, __import__(tmp).app)

@root.route('/')
def handle_index():
    txt="<div style='font-weight:normal;color:blue;float:left;width:345px;text-align:center;border:1px solid silver;background:#E8EFFF;padding:8px;font-size:14px;font-family:Tahoma'>欢迎使用<span style='font-weight:bold;color:red'>artwebs</span>系统网站快速开发平台</div>"
    return txt

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

@root.route('/css/<filename>')
def css(filename):
    return static_file(filename, root=CSS_FILE_PATH)

@root.route('/css/<path:path>')
def js(path):
    return static_file(path, root=CSS_FILE_PATH)

@root.route('/center')
def handel_redirect():
    return redirect(request.path+'/')



# http://localhost:8081/Aws/validate_user?cmd=admin
# http://localhost:8081/Aws/validate_user?a=12&b=1233
# http://localhost:8081/Aws/aws_test?a=12&b=1233
# http://localhost:8081/<action:re:[A-Z][a-z]+>/<method:re:[a-z]+>
@root.route('/<action:re:[A-Z]\w+>/<method:re:\w+>',method=['post','get'])
def action(action,method):
    action+="Action"
    __import__(action)
    aMod = sys.modules[action]
    aClass= getattr(aMod, action)
    if hasattr(aClass,method):
        aMethod=getattr(aClass(),method)
        return aMethod()
    else:
        aMethod=getattr(aClass(),"defaultExec")
        return aMethod(method)



@error(404)
def error404(error):
    return 'Nothing here, sorry'


def getParam():
    cmd=request.POST.get('cmd')
    if cmd is None :
        cmd=request.GET.get('cmd')
    if cmd is None :
        poskey=request.POST.keys()
        getkey=request.GET.keys()
        rsdic={}
        import json
        for item in poskey:
            rsdic[item]=request.POST.get(item)
        for item in getkey:
            rsdic[item]=request.GET.get(item)
        cmd=json.dumps(rsdic)
    return cmd

session_opts = {
"session.type": "file",
'session.cookie_expires': True,
'session.auto': True,
'session.data_dir': "cache",
}
root = SessionMiddleware(root, session_opts)



if __name__ == '__main__':    
    debug(True)
    run(root, host="0.0.0.0",reloader=True)
