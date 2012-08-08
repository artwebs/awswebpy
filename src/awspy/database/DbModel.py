'''
Created on 2010-11-9

@author: Administrator
'''
from Db import Db
from DbUtil import DbUtil
#from DbOracle import DbOracle
from awspy.object.BinMap import BinMap

class DbModel(Db):
    __util=DbUtil()
    __tablename= None
    '''
    classdocs
    '''


    def __init__(self,tablename=None):
        if tablename is not None: self.__tablename=tablename
        
    def getSelectResult(self,fvs=None,where=None,tableName=None):
        fvpart="*";
        tbname="";
        if fvs is not None:fvpart=self.__util.getSelectPart(fvs)
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="select "+fvpart+" from "+tbname
        if where is not None: sql+=" where "+where
        rs=self.getQuery(sql)
        rs=self.__util.getSelectList(fvs,rs)
        return rs
    
    def getInsertResult(self,fvs=None,tableName=None):
        rs=False
        fvpart=""
        tbname=""
        if fvs is not None:fvpart=self.__util.getInsertPart(fvs)
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="insert into "+tbname+" "+fvpart
        
        rs=self.runExecute(sql)
        return rs
    
    def getUpdateResult(self,fvs=None,where=None,tableName=None):
        rs=False
        fvpart=""
        tbname=""
        if fvs is not None:fvpart=self.__util.getUpdatePart(fvs)
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="update "+tbname+" set "+fvpart
        if where is not None: sql+=" where "+where
        rs=self.runExecute(sql)
        return rs
    
    def getDeleteResult(self,where=None,tableName=None):
        rs=False
        tbname=""
        if tableName is not None:
            tbname=tableName;
        else:
            tbname=self.__tablename
        sql="delete from "+tbname
        if where is not None: sql+=" where "+where
        rs=self.__db.runExecute(sql)
        return rs