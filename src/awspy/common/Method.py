# -*- coding:gbk -*- 
import subprocess    
import re,sys
import socket
import urllib
import base64
import string
import time
import os

#from artsys.http.HttpClient import HttpClient
from artsys.object.LHBMap import LHBMap

'''
服务器检测
'''
def detectHost(host):
    rs="-1"
    p = subprocess.Popen(["ping.exe", host], 
                        stdin = subprocess.PIPE, 
                        stdout = subprocess.PIPE, 
                        stderr = subprocess.PIPE, 
                        shell = True)    
        
    out = p.stdout.read()                                     
    regex = re.compile("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms", re.IGNORECASE)
    arr=regex.findall(out)
    if len(arr)==1:
        rs="00"
    return rs
    
    
'''
端口检测
'''
def detectPort(host,port=80,timeout=30):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(timeout)
    rs="-1"
    try:
        sk.connect((host,port))
        rs="00"
    except Exception:
        rs="-1"
    sk.close()
    return rs
    
def urlencode(str,charset='utf8',ocharset=None):
    if ocharset is None:
        ocharset=sys.getdefaultencoding()
    try :   
        str=urllib.quote(str.decode(sys.getdefaultencoding()).encode(charset))
    except Exception:
        pass
    return str


def urldecode(str,charset='utf8'):
    str=(urllib.unquote(str)).decode(charset)
    return str

def getsyscharset():
    return sys.getdefaultencoding()

def http_parse_query(meg):
    http=LHBMap();
    regex = re.compile("(GET|POST)\s+(.+?)\s+(.+?)\r\n", re.IGNORECASE)
    out=regex.findall(meg)
    if len(out)>0:
        http.setvalue("HTTP_METHOD", out[0][0])
        http.setvalue("HTTP_QUERY_STRING", out[0][1])
        http.setvalue("HTTP_PROTOCOL", out[0][2])
    else:
        http.setvalue("HTTP_METHOD", "")
        http.setvalue("HTTP_QUERY_STRING", "")
        http.setvalue("HTTP_PROTOCOL", "")
    http_parse_query_item(meg,"Accept:\s+(.+?)\r\n",http,"HTTP_ACCEPT")
    http_parse_query_item(meg,"Accept-Language:\s+(.+?)\r\n",http,"HTTP_ACCEPT_LANGUAGE")
    http_parse_query_item(meg,"User-Agent:\s+(.+?)\r\n",http,"HTTP_USER_AGENT")
    http_parse_query_item(meg,"Content-Type:\s+(.+?)\r\n",http,"HTTP_CONTENT_TYPE")
    http_parse_query_item(meg,"Accept-Encoding:\s+(.+?)\r\n",http,"HTTP_ACCEPT_ENCODING")
    http_parse_query_item(meg,"Host:\s+(.+?)\r\n",http,"HTTP_HOST")
    http_parse_query_item(meg,"Connection:\s+(.+?)\r\n",http,"HTTP_CONNECTION")
    http_parse_query_item(meg,"Content-Length:\s+(.+?)\r\n",http,"HTTP_CONNECTION_LENGTH")
    http_parse_query_item(meg,"Cache-Control:\s+(.+?)\r\n",http,"HTTP_CACHE_CONTROL")
    regex = re.compile("\r\n\r\n(.+)", re.IGNORECASE)
    out=regex.findall(meg)
    if len(out)>0:
        http.setvalue("HTTP_POST_VARS", out[0])
    else:
        http.setvalue("HTTP_POST_VARS", "")
    return http        
       
    
def http_parse_query_item(meg,reg,http,itemname):
    regex = re.compile(reg, re.IGNORECASE)
    out=regex.findall(meg)
    if len(out)>0:
        http.setvalue(itemname, out[0])
    else:
            http.setvalue(itemname, "")

def http_queryobject(httpMap):   
    querystring="";
    regex = re.compile(".+\?(.+)", re.IGNORECASE)
    out=regex.findall(httpMap.getvalue("HTTP_QUERY_STRING"))
    if len(out)>0:
        querystring="&"+out[0]
    if  httpMap.getvalue("HTTP_POST_VARS")!="":
        querystring="&"+httpMap.getvalue("HTTP_POST_VARS")
        
    regex = re.compile("&(\w+)=([^&]+)", re.IGNORECASE)
    out=regex.findall(querystring)
    queryobject=LHBMap()
    queryobject.clear()
    for i in range(len(out)):
        queryobject.put(out[i][0], out[i][1])
    return queryobject

def readfile(filename):
    rs="";
    file_object = open(filename)
    try:
        rs = file_object.read()
    finally:
        file_object.close()
    return rs;


'''

'''
def console_log(txt,path="d:/palmlink/pylog",filetop="",code='gbk'):
    try:
        txt=(txt.decode(code)).encode('utf8')
    except:
        pass
    if not os.path.isdir(path):  
        os.mkdir(path)  
    date=time.strftime("%Y%m%d",time.localtime())
    fn=path+"/"+filetop+date+".log"
    fd=open(fn,"a")            
    rs="\n"+time.strftime("%Y-%m-%d %X",time.localtime())+" [console] "    
    rs+=txt;        
    fd.write(rs)
    fd.close()
    pass

def test():
#    u=HttpClient()
#    s="锟叫癸拷"
#    print sys.getdefaultencoding()
#    a=urlencode(s);
#    print urldecode(a)
#
#    url="http://localhost:8686/LHBSystem/index.php?aaa="+a
#    print url
#    rs=u.doget(url)
#    print rs[2]
#    print rs
#    print readfile("d:\\temp\\test\\SMSOUT00000000004125.txt")
    console_log('好的',path="d:/palmlink/pylog")


if __name__=="__main__":
    test()

    

        