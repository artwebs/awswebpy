#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, dirname, join
import logging


#logging.basicConfig(level=logging.ERROR,
logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s][%(asctime)s][%(process)d][%(filename)s:%(lineno)d][%(funcName)s] %(message)s',
                    filename=abspath(join(dirname(__file__), "../WebContent/log/site.log")),
                    filemode='a+')


DATABASE = {
    'connstr' : abspath(join(dirname(__file__), "../data/awsdatabase.db")),
    'host' : '127.0.0.1',
    'user' : 'postgres',
    'passwd' : 'windows123',
    'db' : 'awsweb',
}

#网站根域名
ROOT_DOMAIN = '127.0.0.1'

#session相关
SECRET_KEY = 'secret_key_for_test'
SESSION_MAX_AGE = 7200

#管理员邮箱列表
ADMIN_EMAIL_LIST = ['artwebs@163.com']

#指定的模板路径
CUSTOM_TPL_PATH = abspath(join(dirname(__file__), "../WebContent/views/"))

#静态文件
STATIC_FILE_PATH = abspath(join(dirname(__file__), "../WebContent/static/"))
IMAGES_FILE_PATH = abspath(join(dirname(__file__), "../WebContent/images/"))
JS_FILE_PATH = abspath(join(dirname(__file__), "../WebContent/js/"))
CSS_FILE_PATH = abspath(join(dirname(__file__), "../WebContent/css/"))
UPLOAD_FILE_PATH = abspath(join(dirname(__file__), "../WebContent/upload/"))