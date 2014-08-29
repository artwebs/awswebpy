# -*- coding: utf-8 -*-
__author__ = 'artwebs'
from Src.action.AwsAction import AwsAction
import hashlib

#设置参数
token=""
appid=""
secret=""
class WeiXinApiAction(AwsAction):
    def defaultExec(self,fun):
        check=self.checkSignature()
        print check
        if check:
            pass

        return check

    def default(self):
        check=self.checkSignature()
        para=self.getParam()
        if check:
            if para.has_key("echostr"):
                return para["echostr"]
        else:
            pass


    def checkSignature(self):
        para=self.getParam()
        print para
        paraArr=[token,para["timestamp"],para["nonce"]]
        # paraArr=["ddfafds","aadfdsa","f"]
        paraArr.sort()
        tmpStr="".join(paraArr)
        tmpStr=hashlib.sha1(tmpStr).hexdigest()
        if tmpStr==para["signature"]:
            return True;
        else:
            return False;


    def revUserMessage(self):
        print self.getParam()



if __name__ == '__main__':
    from awspy.Utils.Utils import *
    rsarr=https("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+appid+"&secret="+secret)
    print rsarr
    access_token="";
    import json
    if rsarr[0]==200:
        dic=json.loads(rsarr[2])
        access_token=dic["access_token"]
    else:
        print "获取 access_token 失败"
        exit();
    print "access_token="+access_token

    from awspy.Utils.Utils import *
    para='{"button":[{"type":"click","name":"今日歌曲","key":"V1001_TODAY_MUSIC"},{"type":"click","name":"歌手简介","key":"V1001_TODAY_SINGER"},{"name":"菜单","sub_button":[{"type":"view","name":"搜索","url":"http://www.soso.com/"},{"type":"view","name":"视频","url":"http://v.qq.com/"},{"type":"click","name":"赞一下我们","key":"V1001_GOOD"}]}]}'
    para=urlencode(para)
    # rs=obj.dopostContent("https://api.weixin.qq.com/cgi-bin/menu/create?access_token="+access_token.encode('utf8'),para)
    rs=https("https://api.weixin.qq.com/cgi-bin/menu/create?access_token="+access_token.encode('utf8'),'POST',para)
    print rs
