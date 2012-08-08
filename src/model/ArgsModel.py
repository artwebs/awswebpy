# -*- coding: utf-8 -*-
from depend.artsys import SqliteModel,BinMap,BinMap,ActionJson,BinList
from conf.setting import DATABASE
import json

model=SqliteModel(DATABASE['connstr'])

class ArgsModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getVersionApksize(self):
        rs=BinMap()
        inpara=BinMap()
        inpara.put('args_id','')
        inpara.put('args_content','')
        rslist=model.getSelectResult(inpara, "args_id='version' or args_id='apk_size'",'args')
        for i in range(0,rslist.size()):
            rs.put(rslist.getvalue(i,'args_id'),rslist.getvalue(i,'args_content'));
        return rs;
        