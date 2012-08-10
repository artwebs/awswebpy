'''
Created on 2010-11-9

@author: Administrator
'''
import re
from awspy.object.BinMap import BinMap 
from awspy.object.BinList import BinList 
class DbUtil(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getSelectPart(self,fieldMap):
        rs=""
        num=fieldMap.size()
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None and re.search("\s+as\s+", field) is None:
                fieldarr=field.split(".")
                rs+=fieldarr[0]+","
            else:
                rs+=field+","
        if len(rs)>0:
            rs=rs[0:len(rs)-1]
        return rs
    
    def getSelectList(self,fieldMap,result):
        rslist=BinList()
        num=fieldMap.size()
        fields=[];
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None:
                fieldarr=field.split(".")
                fields.append(fieldarr[0])
            elif re.search("\s+as\s+", field) is not None:
                fieldarr=field.split(" ")
                fields.append(fieldarr[len(fieldarr)-1])
            else:
                fields.append(field)
        line=0
        for rs in result:
            for i in range(len(fields)):
               rslist.put(line,fields[i], rs[i])
            line=line+1
        return rslist
    
    def getInsertPart(self,fieldMap):
        rs=""
        fs=""
        vs=""
        
        num=fieldMap.size()
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None and re.search("\s+as\s+", field) is None:
                fieldarr=field.split(".")
                if fieldarr[1]=="realstring" or fieldarr[1]=="integer":
                    fs+=fieldarr[0]+","
                    vs+=fieldMap.getvalue(num=i)+","
                else:
                    fs+=fieldarr[0]+","
                    vs+="'"+fieldMap.getvalue(num=i)+"',"
                
            else:
                fs+=field+","
                vs+="'"+fieldMap.getvalue(num=i)+"',"
        if len(fs)>0:
            fs=fs[0:len(fs)-1]
        if len(vs)>0:
            vs=vs[0:len(vs)-1]
        rs="("+fs+") values ("+vs+")"
        return rs
    
    def getUpdatePart(self,fieldMap):
        rs=""        
        num=fieldMap.size()
        for i in range(num):
            field=fieldMap.getkey(i)
            if re.search("\.", field) is not None and re.search("\s+as\s+", field) is None:
                fieldarr=field.split(".")
                if fieldarr[1]=="realstring" or fieldarr[1]=="integer":
                    rs+=fieldarr[0]+"="
                    rs+=fieldMap.getvalue(num=i)+","
                else:
                    rs+=fieldarr[0]+"="
                    rs+="'"+fieldMap.getvalue(num=i)+"',"
                
            else:
                rs+=field+"="
                rs+="'"+fieldMap.getvalue(i)+"',"
        if len(rs)>0:
            rs=rs[0:len(rs)-1]
        return rs
    
if __name__=="__main__":
#    print "id.string".index(".")
#    str="id.string"
#    
#    if re.search("\.", str) is not None and re.search("\s+as\s+", str) is None:
#        print str.split(".");
#    rs=re.search("\.", "idstring")
#    print rs
     f=BinMap();
     f.put("id.realstring","1")
     f.put("name.string","2")
     u=DbUtil();
#     print u.getSelectPart(f);
#     print u.getInsertPart(f)
     print u.getUpdatePart(f)