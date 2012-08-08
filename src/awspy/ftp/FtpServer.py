'''
Created on 2010-10-24

@author: Administrator
'''
import os
from artsys.ftp.pyftpdlib import DummyAuthorizer, FTPServer, FTPHandler, __ver__
class FtpServer:
    __host="localhost"
    __port=21
    __homedir="d:"+os.sep+"ftp"
    __maxcons=256
    __masipstep=5
    __perm="elradfmw"
    __authorizer= DummyAuthorizer()


    def __init__(self,host,port,homedir="",maxcons=256,masipstep=5):
        self.__host=host
        self.__port=port
        if homedir!="":
             self.__homedir=homedir       
        if maxcons!=256:
            self.__maxcons=maxcons
        if masipstep!=256:
            self.__masipstep=masipstep
                
    def adduser(self,username,userpwd,homedir="",perm=""):
        if homedir=="":
            homedir= self.__homedir
        if(perm==""):
            perm=self.__perm
        self.__authorizer.add_user(username, userpwd, homedir, perm)
            
            
    
    def addanonymous(self,homedir=""):
        if homedir=="":
            homedir= self.__homedir
        self.__authorizer.add_anonymous(homedir)
        
    def start(self):
            ftp_handler = FTPHandler
            ftp_handler.authorizer = self.__authorizer
   
            # Define a customized banner (string returned when client connects)
            ftp_handler.banner = "pyftpdlib %s based ftpd ready." %__ver__
   
            # Specify a masquerade address and the range of ports to use for
            # passive connections.  Decomment in case you're behind a NAT.
            #ftp_handler.masquerade_address = '151.25.42.11'
            #ftp_handler.passive_ports = range(60000, 65535)
   
            # Instantiate FTP server class and listen to 0.0.0.0:21
            address = (self.__host, self.__port)
            ftpd = FTPServer(address, ftp_handler)
   
            # set a limit for connections
            ftpd.max_cons = self.__maxcons
            ftpd.max_cons_per_ip = self.__masipstep
    
            # start ftp server
            ftpd.serve_forever()


'''
if __name__ == "__main__":
    server=FtpServer("localhost",22,"d:"+os.sep+"ftp/1111")
    server.adduser("www", "123")
    server.start()
'''

    
        
        

        