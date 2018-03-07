﻿# Config
NODE_ID = 编号

#hour,set 0 to disable
SPEEDTEST = 72
CLOUDSAFE = 1
ANTISSATTACK = 0
AUTOEXEC = 0
MULTI_THREAD = 0

MU_SUFFIX = 'SSR'
MU_REGEX = '%5m%id.%suffix'

SERVER_PUB_ADDR = '127.0.0.1' # mujson_mgr need this to generate ssr link
API_INTERFACE = 'glzjinmod' #mudbjson, sspanelv2, sspanelv3, sspanelv3ssr, muapiv2(not support)

#mudb
MUDB_FILE = 'mudb.json'

# Mysql
MYSQL_HOST = '数据库的服务器ip'
MYSQL_PORT = 3306
MYSQL_USER = '用户'
MYSQL_PASS = '密码'
MYSQL_DB = '用户'
MYSQL_UPDATE_TIME = 60

MYSQL_SSL_ENABLE = 0
MYSQL_SSL_CA = ''
MYSQL_SSL_CERT = ''
MYSQL_SSL_KEY = ''

# API
API_HOST = '127.0.0.1'
API_PORT = 80
API_PATH = '/mu/v2/'
API_TOKEN = 'abcdef'
API_UPDATE_TIME = 60

#Safety
IP_MD5_SALT = 'randomforsafety'

# Manager (ignore this)
MANAGE_PASS = 'ss233333333'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 23333
