# -*- coding: utf-8 -*-
from depend.artsys import SqliteModel,BinMap,BinMap,ActionJson,BinList
from conf.setting import DATABASE
import json

model=SqliteModel(DATABASE['connstr'])

class UserModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def verfiyUser(self,user_id,user_pwd,imei,imsi):
        rs=BinMap()
        inpara=BinMap()
        inpara.put('user_id','')
        inpara.put('user_pwd','')
        inpara.put('imei','')
        inpara.put('imsi','')
        rslist=BinList()
        rslist=model.getSelectResult(inpara, "user_id='"+user_id+"' and user_pwd='"+user_pwd+"'",'users')
        if rslist.size()==1:
            if (rslist.getvalue(0,'imei')=="" and rslist.getvalue(0,'imsi')=="") or (rslist.getvalue(0,'imei')==None and rslist.getvalue(0,'imsi')==None):
                inpara.clear()
                inpara.put('imei',imei)
                inpara.put('imsi',imsi)
                print inpara.getitem()
                model.getUpdateResult(inpara, "user_id='"+user_id+"' and user_pwd='"+user_pwd+"'",'users')
                rs.put('code','1')
                rs.put('message','登录成功')
            elif rslist.getvalue(0,'imei')==imei and rslist.getvalue(0,'imsi')==imsi:
                rs.put('code','1')
                rs.put('message','登录成功')
                
            else:
                rs.put('code','0')
                rs.put('message','手机已经绑定，违法终端')
        else:
            rs.put('code','0')
            rs.put('message','用户名或密码错误')
        return rs;
    
    def changPassWord(self,user_id,oldpwd,newpwd):
        inpara=BinMap()
        inpara.put('user_id','')
        inpara.put('user_pwd','')
        inpara.put('imei','')
        inpara.put('imsi','')
        rslist=BinList()
        rs=BinMap()
        rslist=model.getSelectResult(inpara, "user_id='"+user_id+"' and user_pwd='"+oldpwd+"'",'users')
        if rslist.size()==1:  
            inpara.clear()      
            inpara.put('user_pwd',newpwd)
            model.getUpdateResult(inpara, "user_id='"+user_id+"'",'users')
            rs.put('code','1')
            rs.put('message','修改成功')
        else:
            rs.put('code','0')
            rs.put('message','用户名或密码错误')
        return rs;
        
