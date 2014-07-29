__author__ = 'artwebs'
from Src.model.DefaultSqliteModel import *
from depend.bottle import request

class DefaultJSONAction(object):
    def login(self):
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

    def changePassword(self):
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