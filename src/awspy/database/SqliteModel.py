#coding=utf-8
from awspy.database.Db import Db
from awspy.database.DbModel import DbModel
from awspy.object.BinMap import BinMap
import sqlite3

class SqliteModel(DbModel):    

    def __init__(self):
        '''
        Constructor
        '''
    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        Db.__init__(self,connstr,host,user,passwd,db)
        
    def getCursor(self):
        self.conn= sqlite3.connect(self.connstr)
        self.cursor = self.conn.cursor()