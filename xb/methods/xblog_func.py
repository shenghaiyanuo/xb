__author__ = 'piglet'

from xb.methods.mysql_class import MysqlConnect
from xb.settings import MYSQL_XBLOG
from hashlib import md5

import datetime

class App_log(object):
    def __init__(self):
        self.conn=''
        self.cursor=''

    def __connect(self):
        self.conn=MysqlConnect(**MYSQL_XBLOG)
        self.cursor=self.conn.cursor()


    def __disconect(self):
        self.conn.close()


    def log_user(self,log_tuple):
        self.__connect()
        sql = 'insert into log_user values %s ' % str(log_tuple)
        self.cursor.execute(sql)
        self.conn.commit()
        self.__disconect()


def log_user(func):
    def _log_user(request):
        POST=request.POST
        # print POST
        user_phone=str(POST['user_phone'])
        user_location = str(POST['user_location'])
        user_device = str(POST['user_device'])
        user_action = str(request).split('/')[2]
        ret = func(request)
        user_status= str(eval(ret.content)['status'])
        user_code = str(eval(ret.content)['code'])
        user_ret = str(eval(ret.content)['ret'])
        user_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        action_id = md5(user_phone+user_time).hexdigest()
        log = MysqlConnect()
        log_tuple= (action_id,user_phone,user_action,user_device,user_location,user_status,user_code,user_ret,user_time)
        log.log_user(log_tuple)
        return ret
    return _log_user
