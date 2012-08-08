'''
Created on 2010-11-10

@author: Administrator
'''
from Db import Db
from DbModel import DbModel
from artsys.object.LHBMap import LHBMap
import cx_Oracle  

class DbOracle(Db):
    '''
    classdocs
    '''


    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        Db.__init__(self,connstr,host,user,passwd,db)
        
    def getCursor(self):
        self.conn=cx_Oracle.connect(self.connstr)
        self.cursor = self.conn.cursor()    

if __name__=="__main__":
    db=DbOracle("jjoa/adminpolice0871@116.52.157.130:1521/ORCL1")
    model=DbModel(db,"t_count")
    f=LHBMap();
    f.put("countname as tt","newid1")
    f.put("countcontent.string","2")
#    print model.getInsertResult(f)
#    print model.getUpdateResult(f, "countname='newid1'")
    rs=model.getSelectResult(f)
    print rs.getitem()
#
#    print model.getDeleteResult("countname='newid1'")
#    print model.getSelectResult(f)
        