# -*- coding: utf-8 -*-
'''
Created on 2010-10-30

@author: Administrator
'''

class BinMap(object):
    __dic={}
    '''
    classdocs
    '''


    def __init__(self):
        self.__dic={}
        '''
        Constructor
        '''
        
    def put(self,key,value):
        dic={key:value}
        self.__dic.setdefault(key,value)
        
    def getvalue(self,key=None,num=None):
        rs=None
        if key!=None:
            rs=self.__dic[key]
        elif num!=None:
            rs=self.__dic[self.__dic.keys()[num]]
                    
        return rs;
    
    def getkey(self,num=None):
        rs=None
        if num!=None:
            rs=self.__dic.keys()[num]                    
        return rs;
    
    def setvalue(self,key=None,value=None,num=None):
        flag=False
        if key!=None:
            self.__dic.setdefault(key,value)            
        elif num!=None:
            self.__dic.setdefault(self.__dic.keys()[num],value)
        if not flag:
            self.put(key, value)
            
    def deletevalue(self,key=None,num=None):
        flag=True
        if key!=None:
            self.__dic.pop(key)
        elif num!=None:
            self.__dic.pop(self.__dic.keys()[num])
        else :
            flag=False
             
    def isexists(self,key=None,num=None):
        flag=False
        if key!=None:
           flag=self.__dic.has_key(key)           
        elif num!=None:
            if num<range(self.__dic) :
                flag=True
        return flag
                
    def getitem(self):
        return self.__dic
    
    def clear(self):
        self.__dic.clear()
    
    def size(self):
        return len(self.__dic)
    
    
if __name__=="__main__":
    test()
    
    
    
    
        
        
        
        