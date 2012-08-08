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

@app.route('/changePassword',method = 'POST')
def changePassword():
    login_name=request.forms.get('login_name')
    oldpwd=request.forms.get('oldpwd')
    newpwd=request.forms.get('newpwd')
    rs=BinMap()
    if oldpwd==newpwd :
        rs.put('code','0')
        rs.put('message','新旧密码相同')
    else:
        user=UserModel()
        rs=user.changPassWord(login_name,oldpwd,newpwd)
    return json.dumps(rs.getitem())