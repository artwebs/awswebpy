class Db(object):
    '''
    classdocs
    '''
    conn=None
    cursor=None
    connstr=None
    host=None
    user=None
    passwd=None
    db=None
    

    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None):
        self.connstr=connstr
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
        
    def getCursor(self):
        pass
    
    def runExecute(self,sql):
        rs=False
        self.getCursor()
        self.cursor.execute(sql)
        rscount=self.cursor.rowcount
        self.conn.commit()
        self.closeCursor();
        if rscount>0:
            rs=True
        return rs
    
    def getQuery(self,sql):
        self.getCursor()
        self.cursor.execute(sql) 
        rs = self.cursor.fetchall() 
        self.closeCursor();
        return rs
    
    def closeCursor(self):
        self.cursor.close();
        self.conn.close(); 
        