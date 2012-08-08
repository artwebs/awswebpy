'''
Created on 2010-10-30

@author: Administrator
'''

class BinList(object):
    __list=[]
    '''
    classdocs
    '''


    def __init__(self):
        pass
        
    def put(self,num,key,value,flag=True):
        if num is not None:
            if num>=len(self.__list):
                dic={key:value}
                self.__list.append(dic)
            else:
                dic=self.__list[num]
                dic[key]=value
        else:
            if flag:
                dic={key:value}
                self.__list.append(dic)
            else:
                dic=self.__list[len(self.__list)-1]
                dic[key]=value
            

        
        
    def getvalue(self,num,key):
        rs=None
        if num<len(self.__list):
            dic=self.__list[num]
            rs=dic.get(key)       
                    
        return rs;
    
    def setvalue(self,num,key,value):
        flag=False
        if num<len(self.__list):
            dic=self.__list[num]
            dic[key]=value
        else:
            dic={key:value}
            self.__list.append(dic)
            
    def deletevalue(self,num,key=None):
        if key is None:
            if num<len(self.__list):
                self.__list.pop(num)
        else:
            if num<len(self.__list):
                dic=self.__list[num]
                if dic.has_key(key):
                    dic.pop(key)        
       
    def isexists(self,num,key):
        flag=False
        if num<len(self.__list):
            dic=self.__list[num]
            flag=dic.has_key(key)
        return flag
                
    def getitem(self):
        return self.__list
    
    def clear(self):
        self.__list=[]
    
    def size(self):
        return len(self.__list)
    

                    
def test():
    list=LHBList()
    list.put(0,"a","1");
    list.put(0,"b","2");    
    list.put(1,"c","3");
    list.put(1,"d","4"); 
    list.deletevalue(1,"c")
   
    print list.getvalue(1,"d")
    print list.isexists(1,"d")
    print list.getitem()
    list.setvalue(1,"c","55")
    print list.getitem()
    
if __name__=="__main__":
    test()  