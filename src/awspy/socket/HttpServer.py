import re
from artsys.object.LHBMap import LHBMap
from artsys.socket.SocketServer import *
from artsys.common.Method import *
class HttpServer(SocketServer):
    httpMap=None
    queryMap=None

    def __init__(self,port=None,host=None,listen_num=None,time_out=None,rev_max=None):
        SocketServer.__init__(self,port,host,listen_num,time_out,rev_max)
        
    def run(self): 
        try:
            while 1:       
                meg=self.revmessage()                
                self.httpMap=http_parse_query(meg)
                self.queryMap=http_queryobject(self.httpMap)
                rs="HTTP/1.1 200 OK\r\n\r\n"
                try:                    
                    rs=rs+self.doquery() 
                except:
                    pass 
                self.sendmessage(rs)
                self.closeconn()                   
                    
        except:
            self.closeconn()  
    
    def doquery(self):
        return "This a query method"
    

class test(HttpServer):
    def doquery(self):
        return "test"
   
if __name__=="__main__":
    t=test()
    t.start()
        