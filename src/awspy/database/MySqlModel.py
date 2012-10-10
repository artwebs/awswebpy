#coding=utf-8
import MySQLdb
from Db import Db
from DbModel import DbModel
from awspy.object.BinMap import BinMap
class MySqlModel(DbModel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None,port=None):
        Db.__init__(self,connstr,host,user,passwd,db,port)
        
    def getCursor(self):
        if self.port is not None:
            self.conn= MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,charset="utf8")
        else:
            self.conn= MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,charset="utf8")
        self.cursor = self.conn.cursor()   
#        self.runExecute("set names 'utf8'");
        
if __name__=="__main__":
    db=MySqlModel(host='localhost', user='root',passwd='windows123',db='psdemo')
#    model=DbModel(db,"users")
    f=BinMap();
    f.put("userid","newid1")
    f.put("name","2")
#    print model.getInsertResult(f)
#    print model.getSelectResult(f)
#    
#    print model.getUpdateResult(f, "countname='newid1'")
    print (db.getSelectResult(f,'1=1','users')).getitem()

#    print model.getDeleteResult("countname='newid1'")
#    print model.getSelectResult(f)