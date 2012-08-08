import win32serviceutil
import win32service
import win32event
import time
import string
import threading

class NTServer(win32serviceutil.ServiceFramework):
    _svc_name_ = "LHBserver"
    _svc_display_name_ = "LHBserver"
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
         th =self.__thread          
         th.start()     
         win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
         
class work(threading.Thread):    
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            fn="d:/python/111.txt"
            fd=open(fn,"a")
            rs="\r\n"+time.strftime("%Y-%m-%d %X",time.localtime())
            fd.write(rs)
            fd.close()
            time.sleep(2)
            
if __name__=="__main__":    
    win32serviceutil.HandleCommandLine(test)
         
