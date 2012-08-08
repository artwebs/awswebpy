# -*- coding: utf-8 -*-
import sqlite3
import re
from urlparse import urlparse
import httplib, urllib,os,time
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

class BinList(object):
    __list=[]
    '''
    classdocs
    '''


    def __init__(self):
        self.__list=[]
        
    def put(self,num,key,value,flag=True):
        if num is not None:
            if num>=len(self.__list):
                dic={key:value}
                self.__list.append(dic)
            else:
                dic=self.__list[num]
                dic[key]=value
        else:
            if flag:
                dic={key:value}
                self.__list.append(dic)
            else:
                dic=self.__list[len(self.__list)-1]
                dic[key]=value
            

        
        
    def getvalue(self,num,key):
        rs=None
        if num<len(self.__list):
            dic=self.__list[num]
            rs=dic.get(key)       
                    
        return rs;
    
    def setvalue(self,num,key,value):
        flag=False
        if num<len(self.__list):
            dic=self.__list[num]
            dic[key]=value
        else:
            dic={key:value}
            self.__list.append(dic)
            
    def deletevalue(self,num,key=None):
        if key is None:
            if num<len(self.__list):
                self.__list.pop(num)
        else:
            if num<len(self.__list):
                dic=self.__list[num]
                if dic.has_key(key):
                    dic.pop(key)        
       
    def isexists(self,num,key):
        flag=False
        if num<len(self.__list):
            dic=self.__list[num]
            flag=dic.has_key(key)
        return flag
                
    def getitem(self):
        return self.__list
    
    def clear(self):
        self.__list=[]
    
    def size(self):
        return len(self.__list)
    
class BinMap(object):
    __dic={}
    '''
    classdocs
    '''


    def __init__(self):
        self.__dic={}
        '''
        Constructor
        '''
        
    def put(self,key,value):
        dic={key:value}
        self.__dic.setdefault(key,value)
        
    def getvalue(self,key=None,num=None):
        rs=None
        if key!=None:
            rs=self.__dic[key]
        elif num!=None:
            rs=self.__dic[self.__dic.keys()[num]]
                    
        return rs;
    
    def getkey(self,num=None):
        rs=None
        if num!=None:
            rs=self.__dic.keys()[num]                    
        return rs;
    
    def setvalue(self,key=None,value=None,num=None):
        flag=False
        if key!=None:
            self.__dic.setdefault(key,value)            
        elif num!=None:
            self.__dic.setdefault(self.__dic.keys()[num],value)
        if not flag:
            self.put(key, value)
            
    def deletevalue(self,key=None,num=None):
        flag=True
        if key!=None:
            self.__dic.pop(key)
        elif num!=None:
            self.__dic.pop(self.__dic.keys()[num])
        else :
            flag=False
             
    def isexists(self,key=None,num=None):
        flag=False
        if key!=None:
           flag=self.__dic.has_key(key)           
        elif num!=None:
            if num<range(self.__dic) :
                flag=True
        return flag
                
    def getitem(self):
        return self.__dic
    
    def clear(self):
        self.__dic.clear()
    
    def size(self):
        return len(self.__dic)
    
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
    http=BinMap();
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
    queryobject=BinMap()
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


class Db(object):
    '''
    classdocs
    '''
    conn=None
    cursor=None
    connstr=None
    host=None
    user=None
    passwd=None
    db=None

    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        self.connstr=connstr
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
        
    def getCursor(self):
        pass
    
    def runExecute(self,sql):
        rs=False
        self.getCursor()
        self.cursor.execute(sql)
        rscount=self.cursor.rowcount
        self.conn.commit()
        self.closeCursor();
        if rscount>0:
            rs=True
        return rs
    
    def getQuery(self,sql):
        self.getCursor()
        self.cursor.execute(sql) 
        rs = self.cursor.fetchall() 
        self.closeCursor();
        return rs
    
    def closeCursor(self):
        self.cursor.close();
        self.conn.close(); 
        
        
class DbUtil(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getSelectPart(self,fieldMap):
        rs=""
        num=fieldMap.size()
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None and re.search("\s+as\s+", field) is None:
                fieldarr=field.split(".")
                rs+=fieldarr[0]+","
            else:
                rs+=field+","
        if len(rs)>0:
            rs=rs[0:len(rs)-1]
        return rs
    
    def getSelectList(self,fieldMap,result):
        rslist=BinList()
        num=fieldMap.size()
        fields=[];
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None:
                fieldarr=field.split(".")
                fields.append(fieldarr[0])
            elif re.search("\s+as\s+", field) is not None:
                fieldarr=field.split(" ")
                fields.append(fieldarr[len(fieldarr)-1])
            else:
                fields.append(field)
        line=0
        for rs in result:
            for i in range(len(fields)):
               rslist.put(line,fields[i], rs[i])
            line=line+1
        return rslist
    
    def getInsertPart(self,fieldMap):
        rs=""
        fs=""
        vs=""
        
        num=fieldMap.size()
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None and re.search("\s+as\s+", field) is None:
                fieldarr=field.split(".")
                if fieldarr[1]=="realstring" or fieldarr[1]=="integer":
                    fs+=fieldarr[0]+","
                    vs+=fieldMap.getvalue(num=i)+","
                else:
                    fs+=fieldarr[0]+","
                    vs+="'"+fieldMap.getvalue(num=i)+"',"
                
            else:
                fs+=field+","
                vs+="'"+fieldMap.getvalue(i)+"',"
        if len(fs)>0:
            fs=fs[0:len(fs)-1]
        if len(vs)>0:
            vs=vs[0:len(vs)-1]
        rs="("+fs+") values ("+vs+")"
        return rs
    
    def getUpdatePart(self,fieldMap):
        rs=""        
        num=fieldMap.size()
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None and re.search("\s+as\s+", field) is None:
                fieldarr=field.split(".")
                if fieldarr[1]=="realstring" or fieldarr[1]=="integer":
                    rs+=fieldarr[0]+"="
                    rs+=fieldMap.getvalue(num=i)+","
                else:
                    rs+=fieldarr[0]+"="
                    rs+="'"+fieldMap.getvalue(num=i)+"',"
                
            else:
                rs+=field+"="
                rs+="'"+fieldMap.getvalue(num=i)+"',"
        if len(rs)>0:
            rs=rs[0:len(rs)-1]
        return rs
    
class DbModel(Db):
    __util=DbUtil()
    __tablename= None
    '''
    classdocs
    '''


    def __init__(self,tablename=None):
        if tablename is not None: self.__tablename=tablename
        
    def getSelectResult(self,fvs=None,where=None,tableName=None):
        fvpart="*";
        tbname="";
        if fvs is not None:fvpart=self.__util.getSelectPart(fvs)
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="select "+fvpart+" from "+tbname
        if where is not None: sql+=" where "+where
        rs=self.getQuery(sql)
        rs=self.__util.getSelectList(fvs,rs)
        return rs
    
    def getInsertResult(self,fvs=None,tableName=None):
        rs=False
        fvpart=""
        tbname=""
        if fvs is not None:fvpart=self.__util.getInsertPart(fvs)
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="insert into "+tbname+" "+fvpart
        
        rs=self.runExecute(sql)
        return rs
    
    def getUpdateResult(self,fvs=None,where=None,tableName=None):
        rs=False
        fvpart=""
        tbname=""
        if fvs is not None:fvpart=self.__util.getUpdatePart(fvs)
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="update "+tbname+" set "+fvpart
        if where is not None: sql+=" where "+where
        rs=self.runExecute(sql)
        return rs
    
    def getDeleteResult(self,where=None,tableName=None):
        rs=False
        tbname=""
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="delete from "+tbname
        if where is not None: sql+=" where "+where
        rs=self.__db.runExecute(sql)
        return rs
    
class DbOracle(Db):
    '''
    classdocs
    '''


    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        Db.__init__(self,connstr,host,user,passwd,db)
        
    def getCursor(self):
        self.conn=cx_Oracle.connect(self.connstr)
        self.cursor = self.conn.cursor()   

class Model(object):    
    '''
    classdocs
    '''
    def __init__(self,top=None,tableName=None):
        '''
        Constructo
        '''
    
    def getSelectResult(self,fvs=None,where=None,tableName=None):
        pass
    
    def getInsertResult(self,fvs=None,where=None,tableName=None):
        pass
    
    def getUpdateResult(self,fvs=None,where=None,tableName=None):
        pass
    
    def getDeleteResult(self,where=None,tableName=None):\
        pass    
    
class MySqlModel(Db):

    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        Db.__init__(self,connstr,host,user,passwd,db)
        
    def getCursor(self):
        self.conn= MySQLdb.connect(self.host,self.user,self.passwd,self.db)
        self.cursor = self.conn.cursor()    
        
class OracleModel(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''

        
class PgModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
     
class SqliteModel(DbModel):    

    def __init__(self):
        '''
        Constructor
        '''
    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        Db.__init__(self,connstr,host,user,passwd,db)
        
    def getCursor(self):
        self.conn= sqlite3.connect(self.connstr)
        self.cursor = self.conn.cursor()
        
class ActionJson(object):
    '''
    classdocs
    '''
    def __init__(self,top=None,tableName=None):
        '''
        Constructo
        '''
    def getList(self,data,items,args=None):
        rs=BinMap()
        rs.put('code', '1')
        rs.put('message', '数据正常')
        rs.put('count', data.size())
        rs.put('type','list')        
        rows=[]
        for i in range(0,data.size()):
            row=BinMap()
            for j in range(0,items.size()):
                yitem=str(items.getvalue(num=j))   
                p = re.compile(r'\[(\w+)\]')
                for m in p.finditer(yitem):
                    yitem=yitem.replace(str(m.group()),str(data.getvalue(i,str(m.group(1)))))                
                row.put(items.getkey(num=j), yitem)                
            rows.append(row.getitem())
        rs.put('data', rows)
        return rs
        
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
        