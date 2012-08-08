'''
Created on 2010-10-26

@author: Administrator
'''
import socket
class SocketClient:
    __host="localhost"
    __port=8002
    __rev_max=1024
    __socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    def __init__(self,host=None,port=None,rev_max=None):
        if host is not None:
            self.__host=host
        if port is not None:
            self.__port=port
        if rev_max is not None:
            self.__rev_max=rev_max
       
    def start(self):
        
        try: 
            self.__socket.connect((self.__host, self.__port))
            self.run()
        except :
            self.__socket.close()  
                 
    def run(self):
        pass
    
    def sendmssage(self,meg):
        self.__socket.send(meg)
    
    def revmessage(self):
        return self.__socket.recv(self.__rev_max)
    
    def closeconn(self):
        self.__socket.close()  
        


class testclient(SocketClient):
    def run(self):
            self.sendmssage("1")
            print self.revmessage()
            
                    
if __name__ == '__main__': 
    t1=testclient(port=8002)
    t1.start()

    
    
        