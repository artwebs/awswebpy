__author__ = 'artwebs'
from Src.action.AwsAction import AwsAction
from depend.bottle import request
from awspy.security.ArtSecurityDES import *
import json
class AppAction(AwsAction):
    key="X+v!zSwkUloAQ$Gf/n)PVbi7"
    iv="k&dWHiQu"
    def defaultExec(self,fun):
        desObj= ArtSecurityDES(mod=CBC);
        if request.POST.get('cmd') or request.GET.get('cmd'):
            return desObj.encode(json.dumps(AwsAction.defaultExec(self,fun)),self.key,self.iv)
        else:
            return AwsAction.defaultExec(self,fun)

    def getParam(self):
        cmd=request.POST.get('cmd')
        desObj= ArtSecurityDES(mod=CBC);
        if cmd is None :
            cmd=request.GET.get('cmd')

        if cmd is None :
            poskey=request.POST.keys()
            getkey=request.GET.keys()
            rsdic={}
            import json
            for item in poskey:
                rsdic[item]=request.POST.get(item)
            for item in getkey:
                rsdic[item]=request.GET.get(item)
            return  rsdic
        else:
            import json
            rs=json.loads(desObj.decode(cmd,self.key,self.iv))
            return rs
