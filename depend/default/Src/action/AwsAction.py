# -*- coding: utf-8 -*-
__author__ = 'artwebs'
import os
import time
from depend.bottle import Bottle,get,post,request
from conf.setting import UPLOAD_FILE_PATH
from Src.model.AWSDataModel import AWSDataModel
class AwsAction(object):
    def defaultExec(self,fun):
        obj=AWSDataModel()
        return obj.execFun(fun,self.getParam())

    def uploadImage(self):
         upload = request.files.get('upload')
         name, ext = os.path.splitext(upload.filename)
         uppath= UPLOAD_FILE_PATH+'/'+time.strftime('%Y%m%d',time.localtime(time.time()))
         if not os.path.exists(uppath):
             os.mkdir(uppath)
         if ext not in ('.png','.jpg','.jpeg','.PGN','.JPG','.JPEG'):
             return 'File extension not allowed.'
         index=0
         while(True):
             fileName=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))+'_'+str(index)+'.'+ext
             save_path = uppath+'/'+fileName
             if os.path.exists(save_path):
                index=index+1
             else :
                 break
         upload.save(save_path) # appends upload.filename automatically
         return fileName

    def getParam(self):
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