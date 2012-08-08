# -*- coding: utf-8 -*-

from depend.bottle import Bottle,debug, run
from depend.bottle import view
from depend.bottle import redirect, abort, static_file
from depend.bottle import jinja2_template as template
from depend.bottle import request, response, local
from awspy.database.SqliteModel import SqliteModel
from awspy.object import BinMap,BinList
from awspy.object.BinMap import BinMap
from awspy.object.BinList import BinList
from awspy.action.ActionJson import ActionJson
from conf.setting import DATABASE
import json

app = Bottle()
model=SqliteModel(DATABASE['connstr'])
action=ActionJson()

@app.route('/test',method=['POST','GET'])
def movie():
    f=BinMap()
    f.put("id","")
    f.put("title","")
    f.put("rtsp","")
    f.put("lrsj","")
    f.put("img","")
    rs=model.getSelectResult(f, '1=1','movies')
    items=BinMap()
    items.put("text", '[title]\n[lrsj]')
    items.put("id", '[rtsp]')
    items.put("img", '[img]')
    rs=action.getList(rs, items, None)
    return json.dumps(rs.getitem())
