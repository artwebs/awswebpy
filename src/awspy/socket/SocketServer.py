import socket
class SocketServer:
    __host="localhost"
    __port=8001
    __listen_num=10
    __time_out=2
    __rev_max=1024
    __socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __conn=None

    def __init__(self,port=None,host=None,listen_num=None,time_out=None,rev_max=None):
        if port is not None:
            self.__port=port
        if host is not None:
            self.__host=host
        if listen_num is not None:
            self.__listen_num=listen_num
        if time_out is not None:
            self.__time_out=time_out
        if rev_max is not None:
            self.__rev_max=rev_max
    
    def start(self):        
        self.__socket.bind((self.__host, self.__port))  
        self.__socket.listen(self.__listen_num)  
        while True:  
            self.__conn,address = self.__socket.accept()  
            
            try:  
                if self.__time_out!=0:
                    self.__conn.settimeout(self.__time_out) 
                self.run()
                self.__conn.close()
            except socket.timeout:  
                self.sendtimeout()  
                self.__conn.close()
    
    def run(self):
        pass
    def settimeout(self,time=None):
        if time is not None:
            self.__time_out=time
    def sendmessage(self,msg):
        self.__conn.send(msg)  
    
    def revmessage(self):
        buf = self.__conn.recv(self.__rev_max)  
        return buf 
    
    def sendtimeout(self):
        self.sendmessage('time out')
    
    def closeconn(self):
         self.__conn.close()
  
class test(SocketServer):
    def run(self): 
        try:
            while 1:       
                meg=self.revmessage()
#                print meg
#                http_parse_query(meg)
#                meg=meg.replace("\r\n","")
                if(meg=="end"):
                    self.closeconn()  
                else:      
                    if meg=="1" :
                        self.sendmessage('welcome to server!')
                        self.closeconn()
                    else:
                        self.sendmessage("11111")
                        self.closeconn()
                        
                    
        except:
            self.closeconn()           
        #self.closeconn()
        
         

        


                         
if __name__ == '__main__': 
    t=test(8001)
    t.start()

        
 
        