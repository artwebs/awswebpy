import depend.app
from depend.bottle import Bottle,debug, run

from action import root


if __name__ == '__main__':
    debug(True)    
    run(root, host="0.0.0.0", port=8081, reloader=True)    
else:
    # Mod WSGI launch
    application = root
    