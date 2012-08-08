'''
Created on 2010-10-26

@author: Administrator
'''
import  sys, os, zipfile 

class Zip:
    def __init__(self):
        pass
    
    def dozip(self,filename,files=[],savedir=None):        
        f = zipfile.ZipFile(filename, 'w' ,zipfile.ZIP_DEFLATED) 
        for file in files:
            if savedir is not None:
                list=file.split('\\')
                fn=list[len(list)-1]
                f.write(file,fn)
            else:
                f.write(file)
        f.close()
    
    def unzip(self,filename,todir):
        z = zipfile.ZipFile(filename, 'r')
        self.DirCreate(todir)
        for f in z.namelist():
            path = os.path.join(todir, f)
            if path.endswith("/"):
                self.DirCreate(path)
            else:
                file(path, 'wb').write(z.read(f))
            
    def DirCreate(self,dir):
        if not os.path.exists(dir):
            os.mkdir(dir)
                                    
#if __name__=="__main__":
#    z=zip()
##    z.unzip("D:\\python\\zip\\filename.zip", "D:\\python\\zip\\abc\\")
#    files=["D:\\python\\zip\\abc\\1.txt","D:\\python\\zip\\abc\\2.txt","D:\\python\\zip\\abc\\3.txt"]
#    z.dozip("D:\\python\\zip\\filename.zip", files,1)


    
        