from awspy.database import SqliteModel

__author__ = 'artwebs'
from awspy.object import BinMap, BinList
from conf.setting import DATABASE


class DefaultSqliteModel(object):
    model=SqliteModel(DATABASE['connstr'])


class ArgsModel(DefaultSqliteModel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def getVersionApksize(self):
        rs= BinMap()
        inpara= BinMap()
        inpara.put('args_id','')
        inpara.put('args_content','')
        rslist=self.model.getSelectResult(inpara, "args_id='version' or args_id='apk_size'",'args')
        for i in range(0,rslist.size()):
            rs.put(rslist.getvalue(i,'args_id'),rslist.getvalue(i,'args_content'));
        return rs;


class UserModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def verfiyUser(self,user_id,user_pwd,imei,imsi):
        rs= BinMap()
        inpara= BinMap()
        inpara.put('user_id','')
        inpara.put('user_pwd','')
        inpara.put('imei','')
        inpara.put('imsi','')
        rslist= BinList()
        rslist=self.model.getSelectResult(inpara, "user_id='"+user_id+"' and user_pwd='"+user_pwd+"'",'users')
        if rslist.size()==1:
            if (rslist.getvalue(0,'imei')=="" and rslist.getvalue(0,'imsi')=="") or (rslist.getvalue(0,'imei')==None and rslist.getvalue(0,'imsi')==None):
                inpara.clear()
                inpara.put('imei',imei)
                inpara.put('imsi',imsi)
                print inpara.getitem()
                self.model.getUpdateResult(inpara, "user_id='"+user_id+"' and user_pwd='"+user_pwd+"'",'users')
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
        inpara= BinMap()
        inpara.put('user_id','')
        inpara.put('user_pwd','')
        inpara.put('imei','')
        inpara.put('imsi','')
        rslist= BinList()
        rs= BinMap()
        rslist=self.model.getSelectResult(inpara, "user_id='"+user_id+"' and user_pwd='"+oldpwd+"'",'users')
        if rslist.size()==1:
            inpara.clear()
            inpara.put('user_pwd',newpwd)
            self.model.getUpdateResult(inpara, "user_id='"+user_id+"'",'users')
            rs.put('code','1')
            rs.put('message','修改成功')
        else:
            rs.put('code','0')
            rs.put('message','用户名或密码错误')
        return rs;