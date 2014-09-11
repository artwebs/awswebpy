# -*- coding: utf-8 -*-
__author__ = 'artwebs'
from Src.action.AwsAction import *
from depend.bottle import template,redirect,request
from Src.model.AWSModel import AWSModel
import json


class ManagerAction(AwsAction):
    def defaultExec(self,fun):
        return template(self.getTplName(fun), param=self.getParamToJson())

    def default(self):
        return template(self.getTplName(self.getCurFunName()), child='mananger_test.html')

    def loginVerfiy(self):
        rs=self.queryData("aws_verfiy_user")
        if rs["code"]==1:
            session = request.environ['beaker.session']
            session['login_name']=rs["result"]["login_name"]
            return redirect("/MgrBCard/default")
        else:
            return redirect("/Manager/default")

    def verfiy(self):
        session = request.environ['beaker.session']
        if session is not None and session.has_key("login_name") :
            if session["login_name"] is not None:
                return ;
        self.redirectUrl()

    def redirectUrl(self,url="/Manager/default"):
        return redirect("/Manager/default")

    def queryData(self,fun):
        obj=AWSModel()
        return obj.execFun(fun,self.getParamToJson())

    def loginOut(self):
        session = request.environ['beaker.session']
        session.delete()
        self.redirectUrl()

