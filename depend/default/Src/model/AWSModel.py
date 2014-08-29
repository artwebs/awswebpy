# -*- coding: utf-8 -*-
__author__ = 'artwebs'
from awspy.database.PgModel import PgModel
from conf.setting import DATABASE
from awspy.object.BinMap import BinMap
import json

class AWSModel(object):
    db=PgModel(host=DATABASE['host'], user=DATABASE['user'],passwd=DATABASE['passwd'],db=DATABASE['db'])

    def execFun(self,fun,str):
        f= BinMap()
        f.put("ojson","")
        rs=self.db.callproc("aws_entrance",[fun,str],f)
        rs=rs.getvalue(0,"ojson")
        print(rs)
        return json.loads(rs)