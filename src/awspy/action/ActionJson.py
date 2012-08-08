#coding=utf-8
import re
from awspy.object.BinMap import BinMap 
from awspy.object.BinList import BinList 
class ActionJson(object):
    '''
    classdocs
    '''
    def __init__(self,top=None,tableName=None):
        '''
        Constructo
        '''
    def getList(self,data,items,args=None):
        rs=BinMap()
        rs.put('code', '1')
        rs.put('message', '数据正常')
        rs.put('count', data.size())
        rs.put('type','list')        
        rows=[]
        for i in range(0,data.size()):
            row=BinMap()
            for j in range(0,items.size()):
                yitem=str(items.getvalue(num=j))   
                p = re.compile(r'\[(\w+)\]')
                for m in p.finditer(yitem):
                    yitem=yitem.replace(str(m.group()),str(data.getvalue(i,str(m.group(1)))))                
                row.put(items.getkey(num=j), yitem)                
            rows.append(row.getitem())
        rs.put('data', rows)
        return rs
        