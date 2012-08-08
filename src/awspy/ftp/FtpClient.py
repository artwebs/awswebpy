# -*- encoding: gb2312 -*-
import ftplib, os, traceback, glob
class FtpClient:
    def __init__( self, ip, port, user, pwd, path='' ):
        """ 开启FTP并进入指定目录 """
        self.ftp = ftplib.FTP()
        self.ftp.connect( ip, port )
        self.ftp.login( user, pwd )
        if path <> '':
            self.path = path
            self.ftp.cwd( path )
    
    def close( self ):
        """ 关闭FTP """
        self.ftp.quit()
    
    def _allFiles( self, search_path, pattern, pathsep=os.pathsep ):
        """ 查找指定目录下符合指定模式的所有文件,以列表形式返回
            @param search_path  查询目录列表
            @param pattern      文件名模式
            @param pathsep      目录分隔符
        """
        for path in search_path.split( pathsep ):
            for match in glob.glob( os.path.join(path, pattern) ):
                yield match
    
    def searchFileFromFTP( self, pattern ):
        """ 在FTP的指定目录下查找文件
            @param pattern  文件名模式
        """
        flist = []
        try:
            self.ftp.dir( pattern, flist.append )
        except:
            flist = []
        # 提取文件名，格式如：-rw-r--r--    1 500      502           881 Aug 29 09:16 AllTest.py
        namelist = []
        for l in flist:
            name = l.split( ' ' )[-1]
            namelist.append( name )
        return namelist
    
    def upload( self, fromdir, pattern ,method='lines'):
        """ 上传文件
            @param fromdir  本地文件目录
            @param pattern  文件名模式
        """
        if fromdir[-1] <> os.sep:
            fromdir += os.sep
        flist = self._allFiles( fromdir, pattern )
        for f in flist:
            try:
                name = f.split( os.sep )[-1]
                print '正在上传:', name
                if method=='binary':
                    self.ftp.storbinary( 'stor ' + name, file( fromdir + name ) )
                else: 
                    self.ftp.storlines( 'stor ' + name, file( fromdir + name ) )
                
            except:
                print '上传文件[%s]错误!' % name
                return False
        return True
        
    def download( self, todir, pattern, isBin=False ):
        """ 下载文件.注意:文件名中带中文的下载不下来
            @param todir        下载到本地的目录
            @param pattern      文件名,可以使用通配符批量下载文件
            @param isBin        是否是二进制文件.是=True;否=False
        """
        # 若目录最后不是'\',则补充之
        if todir[-1] <> os.sep:
            todir += os.sep
            
        flist = self.searchFileFromFTP( pattern )
        if len( flist ) == 0:
            print '未找到文件[%s]!' % pattern
            return False
        fn = [] # 将下载到本地的文件列表(带目录)
        for f in flist:
            fn.append( todir + f )
        
        # 循环下载每一个文件
        for i in range( len(fn) ):
            try:
                fp = None
                try:
                    print '正在下载文件:', flist[i]
                    if isBin:   # 二进制文件
                        fp = file( fn[i] , 'wb' )
                        self.ftp.retrbinary( 'retr ' + flist[i], fp.write )
                    else:       # 非二进制文件
                        fp = file( fn[i] , 'w' )
                        l = []
                        self.ftp.retrlines( 'retr ' + flist[i], l.append )
                        for k in l:
                            fp.write( k + '\n' )
                        del l
                finally:
                    if fp:  fp.close()
            except:
                print '下载文件[%s]时出错!' % flist[i]
                return False
        return True
    
    def deleteFileFromFTP( self, pattern ):
        """ 删除文件,注意:文件名不能为中文
            @param pattern  要删除的文件名,可以使用通配符批量删除文件
        """
        flist = self.searchFileFromFTP( pattern )
        if len( flist ) == 0:
            print '未找到文件[%s]!' % pattern
            return False
        for f in flist:
            try:
                print '正在删除文件:', f
                self.ftp.delete( f )
            except:
                print '删除文件[%s]时出错!' % f
                return False
        return True
    
    def renameFileFromFTP( self, oldname, newname ):
        """ 重命名FTP上的某个文件名
            @param oldname  原文件名
            @param newname  欲改成的文件名
        """
        try:
            self.ftp.sendcmd( 'dele %s' % newname )
        except:
            pass
        
        try:
            print '正在将文件[%s]改名为[%s]' % ( oldname, newname )
            self.ftp.sendcmd( 'RNFR ' + oldname )
            self.ftp.sendcmd( 'RNTO %s' % newname )
            return True
        except:
            print '将文件[%s]改名为[%s]时出错!' % ( oldname, newname )
            return False
#=================================================================================================
'''
if __name__ == '__main__':
    ip = '192.168.3.10'
    port = 21
    user = 'zhangjun'
    pwd = 'iamzhangjun'
    path = '/jnhxkh/'
    myftp = FTP( ip, port, user, pwd, path )
    
    # 显式文件列表
    list = myftp.searchFileFromFTP( '*' )
    for i in list:
        print i
    
    if myftp.upload( 'd:\uniplat\log', 'flow_0.log.20080619' ):
        print 'flow_0.log.20080619上传完毕'
    else:
        print 'flow_0.log.20080619上传失败'
    
    if myftp.download( 'E:\programming\Python\FTP的应用\download', '*' ):
       print '下载完毕'
    else:
       print '下载失败'
    
    if myftp.deleteFileFromFTP( '*' ):
       print '删除完毕'
    else:
       print '删除失败'
    
    if myftp.renameFileFromFTP( 'ftp.py', 'myftp.py' ):
       print '改名完毕'
    else:
       print '改名失败'
    
    myftp.close()
'''
if __name__ == '__main__':
    id="SMSOUT00000000004125.zip"
    client=FtpClient('localhost',21,'www','windows123',"/")        
    if client.upload("d:\\temp",id):
        rs="00"
    else:
        rs="-1"
    client.close()