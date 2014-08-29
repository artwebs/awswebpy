# -*- coding: utf-8 -*-
from depend.bottle import debug, run
from awspy.Utils.FileUtils import *

if __name__ == '__main__':
    if not os.path.exists("Src"):
        copyFiles("depend/default","./")
        print "init finish"
    from Src.action import root
    debug(True)
    run(root, host="0.0.0.0", port=8081, reloader=True)
else:
    # Mod WSGI launch
    from Src.action import root
    application = root

# if __name__=="__main__":
#     print 'hello world'
#     console_log('好的',path="/data/temp/")