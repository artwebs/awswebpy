# -*- encoding: gb2312 -*-
import ftplib, os, traceback, glob
class FtpClient:
    def __init__( self, ip, port, user, pwd, path='' ):
        """ ����FTP������ָ��Ŀ¼ """
        self.ftp = ftplib.FTP()
        self.ftp.connect( ip, port )
        self.ftp.login( user, pwd )
        if path <> '':
            self.path = path
            self.ftp.cwd( path )
    
    def close( self ):
        """ �ر�FTP """
        self.ftp.quit()
    
    def _allFiles( self, search_path, pattern, pathsep=os.pathsep ):
        """ ����ָ��Ŀ¼�·���ָ��ģʽ�������ļ�,���б���ʽ����
            @param search_path  ��ѯĿ¼�б�
            @param pattern      �ļ���ģʽ
            @param pathsep      Ŀ¼�ָ���
        """
        for path in search_path.split( pathsep ):
            for match in glob.glob( os.path.join(path, pattern) ):
                yield match
    
    def searchFileFromFTP( self, pattern ):
        """ ��FTP��ָ��Ŀ¼�²����ļ�
            @param pattern  �ļ���ģʽ
        """
        flist = []
        try:
            self.ftp.dir( pattern, flist.append )
        except:
            flist = []
        # ��ȡ�ļ�������ʽ�磺-rw-r--r--    1 500      502           881 Aug 29 09:16 AllTest.py
        namelist = []
        for l in flist:
            name = l.split( ' ' )[-1]
            namelist.append( name )
        return namelist
    
    def upload( self, fromdir, pattern ,method='lines'):
        """ �ϴ��ļ�
            @param fromdir  �����ļ�Ŀ¼
            @param pattern  �ļ���ģʽ
        """
        if fromdir[-1] <> os.sep:
            fromdir += os.sep
        flist = self._allFiles( fromdir, pattern )
        for f in flist:
            try:
                name = f.split( os.sep )[-1]
                print '�����ϴ�:', name
                if method=='binary':
                    self.ftp.storbinary( 'stor ' + name, file( fromdir + name ) )
                else: 
                    self.ftp.storlines( 'stor ' + name, file( fromdir + name ) )
                
            except:
                print '�ϴ��ļ�[%s]����!' % name
                return False
        return True
        
    def download( self, todir, pattern, isBin=False ):
        """ �����ļ�.ע��:�ļ����д����ĵ����ز�����
            @param todir        ���ص����ص�Ŀ¼
            @param pattern      �ļ���,����ʹ��ͨ������������ļ�
            @param isBin        �Ƿ��Ƕ������ļ�.��=True;��=False
        """
        # ��Ŀ¼�����'\',�򲹳�֮
        if todir[-1] <> os.sep:
            todir += os.sep
            
        flist = self.searchFileFromFTP( pattern )
        if len( flist ) == 0:
            print 'δ�ҵ��ļ�[%s]!' % pattern
            return False
        fn = [] # �����ص����ص��ļ��б�(��Ŀ¼)
        for f in flist:
            fn.append( todir + f )
        
        # ѭ������ÿһ���ļ�
        for i in range( len(fn) ):
            try:
                fp = None
                try:
                    print '���������ļ�:', flist[i]
                    if isBin:   # �������ļ�
                        fp = file( fn[i] , 'wb' )
                        self.ftp.retrbinary( 'retr ' + flist[i], fp.write )
                    else:       # �Ƕ������ļ�
                        fp = file( fn[i] , 'w' )
                        l = []
                        self.ftp.retrlines( 'retr ' + flist[i], l.append )
                        for k in l:
                            fp.write( k + '\n' )
                        del l
                finally:
                    if fp:  fp.close()
            except:
                print '�����ļ�[%s]ʱ����!' % flist[i]
                return False
        return True
    
    def deleteFileFromFTP( self, pattern ):
        """ ɾ���ļ�,ע��:�ļ�������Ϊ����
            @param pattern  Ҫɾ�����ļ���,����ʹ��ͨ�������ɾ���ļ�
        """
        flist = self.searchFileFromFTP( pattern )
        if len( flist ) == 0:
            print 'δ�ҵ��ļ�[%s]!' % pattern
            return False
        for f in flist:
            try:
                print '����ɾ���ļ�:', f
                self.ftp.delete( f )
            except:
                print 'ɾ���ļ�[%s]ʱ����!' % f
                return False
        return True
    
    def renameFileFromFTP( self, oldname, newname ):
        """ ������FTP�ϵ�ĳ���ļ���
            @param oldname  ԭ�ļ���
            @param newname  ���ĳɵ��ļ���
        """
        try:
            self.ftp.sendcmd( 'dele %s' % newname )
        except:
            pass
        
        try:
            print '���ڽ��ļ�[%s]����Ϊ[%s]' % ( oldname, newname )
            self.ftp.sendcmd( 'RNFR ' + oldname )
            self.ftp.sendcmd( 'RNTO %s' % newname )
            return True
        except:
            print '���ļ�[%s]����Ϊ[%s]ʱ����!' % ( oldname, newname )
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
    
    # ��ʽ�ļ��б�
    list = myftp.searchFileFromFTP( '*' )
    for i in list:
        print i
    
    if myftp.upload( 'd:\uniplat\log', 'flow_0.log.20080619' ):
        print 'flow_0.log.20080619�ϴ����'
    else:
        print 'flow_0.log.20080619�ϴ�ʧ��'
    
    if myftp.download( 'E:\programming\Python\FTP��Ӧ��\download', '*' ):
       print '�������'
    else:
       print '����ʧ��'
    
    if myftp.deleteFileFromFTP( '*' ):
       print 'ɾ�����'
    else:
       print 'ɾ��ʧ��'
    
    if myftp.renameFileFromFTP( 'ftp.py', 'myftp.py' ):
       print '�������'
    else:
       print '����ʧ��'
    
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