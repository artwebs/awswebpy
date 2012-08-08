#coding=utf-8
import MySQLdb
from Db import Db
from DbModel import DbModel
from artsys.object.LHBMap import LHBMap
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
        
if __name__=="__main__":
    db=MySqlModel(host='localhost', user='root',passwd='windows123',db='jjydoa')
    model=DbModel(db,"t_count")
    f=LHBMap();
    f.put("countname.string","newid1")
    f.put("countcontent.string","2")
#    print model.getInsertResult(f)
#    print model.getSelectResult(f)
#    
#    print model.getUpdateResult(f, "countname='newid1'")
    print (model.getSelectResult(f)).getitem()

#    print model.getDeleteResult("countname='newid1'")
#    print model.getSelectResult(f)