# -*- coding:gbk -*- 
'''
Created on 2010-10-26

@author: Administrator
'''

from urlparse import urlparse
from artsys.common.Method import *
import httplib, urllib
import re

class HttpClient(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def doget(self,url,args=None,timeout=10):
        arrurl=self.unurl(url)
        rsarr=[]
        if args is None:
            args=self.getargs(arrurl[4])
        hostarr=arrurl[1].split(":")
        host=hostarr[0]
        if len(hostarr)==2:
            port=hostarr[1]
        else:
            port="80"
        conn = httplib.HTTPConnection(host,port,timeout)
        turl=arrurl[2]+"?"+arrurl[4]
        conn.request("GET", turl)
        response = conn.getresponse()       
        data = response.read()        
        data=data.decode("utf8")
        rsarr=[response.status,response.reason,data]
        conn.close()
        return rsarr


    '''
    ('http', 'localhost:8585', '/padd/index.php', '', 'a=0&b=111', '')
    '''    
    def dopost(self,url,args=None,timeout=10,charset='utf8'):
        arrurl=self.unurl(url)
        if args is None:
            args=self.getargs(arrurl[4])
        hostarr=arrurl[1].split(":")
        host=hostarr[0]
        if len(hostarr)==2:
            port=hostarr[1]
        else:
            port="80"
        params = urllib.urlencode(args)
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"} 
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request("POST", arrurl[2], params, headers)
        response = conn.getresponse() 
        data = response.read()
        try:
            data=data.decode(charset)
        except:
            pass
        rsarr=[response.status,response.reason,data]       
        conn.close()
        return rsarr
    
    def unurl(self,url):        
        return urlparse(url)   
    
    def getargs(self,query):
        args={}
        query=query+"&"
        p = re.compile(r'(\w+?)=(.+?)\&') 
        for arr in p.findall(query):
            args.setdefault(arr[0],arr[1])
        return args
        
          
def test():
#    import sys
#    print sys.getdefaultencoding() 


#    url="http://localhost:8585/padd/index.php?a=0&b=111"
#    parsed = urlparse(url)
#    print parsed
#    u=HttpClient()
##    rs=u.doget("http://localhost:8686/LHBSystem/index.php")
#    m=Method();
#    a=m.toencode("中国好的德尔");
#    
#    url="http://localhost:8686/LHBSystem/index.php?aaa="+a;
##    url="http://localhost:8686/LHBSystem/index.php?aaa=中国好的德尔";
#    print url
#    rs=u.dopost(url)
#    rs=u.doget("http://www.126.com")
#    print rs[2]
#    print rs

    hc = HttpClient()        
    rs = hc.dopost("http://localhost/LHBSystem_1/index.php?txt=aaa")



#
if __name__=="__main__": 
    test();





