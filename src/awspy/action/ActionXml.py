# -*- coding: utf-8 -*-
import re
from awspy.object.BinMap import BinMap 
from awspy.object.BinList import BinList 
from awspy.action.Action import *
import xml.dom.minidom

class ActionXml(Action):
    __dom=None;
    __root=None;
    __args=None;

    def __init__(self):
        self.init();
        
    def getList(self,data,items,args=None):
        self.initArgs(args);
        self.appendElement('count', str(data.size()));
        rows=self.appendElement('list')
        for i in range(0,data.size()):
            row=self.appendElement('item')
            for j in range(0,items.size()):
                yitem=str(items.getvalue(num=j))   
                p = re.compile(r'\[(\w+)\]')
                for m in p.finditer(yitem):
                    yitem=yitem.replace(str(m.group()),str(data.getvalue(i,str(m.group(1)))))                
                self.appendElement(items.getkey(num=j),yitem,row)           
            rows.appendChild(row)
        self.__root.appendChild(rows)
        
    def getResult(self,args):
        self.initArgs(args);
        
    def getInfo(self,data,items,args=None):
        self.initArgs(args);
        self.appendElement('count', str(data.size()));
        rows=self.appendElement('data')
        for i in range(0,data.size()):
            content="";
            for j in range(0,items.size()):
                content+="【"+items.getvalue(num=j)+"】"+data.getvalue(i,items.getkey(j));     
                if j is not items.size()-1:
                    content+="\n";
            self.appendElement("row", content, rows)
        self.__root.appendChild(rows)
        
    def init(self):
        impl = xml.dom.minidom.getDOMImplementation()
        self.__dom=impl.createDocument(None, "root", None)
        self.__root=self.__dom.documentElement
        
    def initArgs(self,args):
        self.__args=args;
        if self.__args is None:
            self.__args=BinMap();
            self.__args.put('code', '1');
            self.__args.put('message', '数据下载成功');
        else:
            if not self.__args.isexists('code'):
                self.__args.put('code', '1');
            if not self.__args.isexists('message'):
                self.__args.put('message', '数据下载成功');
        
        for i in range(0,self.__args.size()):
            self.appendElement(self.__args.getkey(i), self.__args.getvalue(num=i))
            
    def appendElement(self,item,text=None,parent=None):
        element=self.__dom.createElement(item);
        if text is not None:
            text=self.__dom.createTextNode(text);
            element.appendChild(text);
        if parent is None:
            self.__root.appendChild(element);
        else:
            parent.appendChild(element);
        return element;
    def reponse(self):
        return self.__dom.toxml('utf-8');