# -*- coding: utf-8 -*-

from depend.bottle import Bottle
from depend.bottle import debug, run
from depend.bottle import view
from depend.bottle import redirect, abort, static_file
from depend.bottle import jinja2_template as template
from depend.bottle import request, response, local
from awspy.database.SqliteModel import SqliteModel
from awspy.object import BinMap,BinList
from awspy.action.ActionJson import ActionJson

from conf.setting import DATABASE
from model.UserModel import UserModel
from model.ArgsModel import ArgsModel
import json
import time

app = Bottle()
model=SqliteModel(DATABASE['connstr'])
action=ActionJson()

@app.route('/login',method = 'POST')
def login():
    login_name=request.forms.get('login_name')
    pwd=request.forms.get('pwd')
    imei=request.forms.get('imei')
    imsi=request.forms.get('imsi')
    user=UserModel()
    rs=user.verfiyUser(login_name,pwd,imei,imsi)    
    args=ArgsModel()
    rsargs=args.getVersionApksize()
    rs.put('version',rsargs.getvalue('version'))
    rs.put('apk_size',rsargs.getvalue('apk_size'))
    return json.dumps(rs.getitem())
