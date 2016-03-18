#coding:utf-8
__author__ = 'piglet'

from mysql.connector import connect
from xb.settings import MYSQL_XB

class MysqlConnect(object):
    def __init__(self):
        self.conn=''
        self.cursor=''
        pass


    def __connect(self):
        self.conn=connect(**MYSQL_XB)
        self.cursor=self.conn.cursor()


    def __disconect(self):
        self.conn.close()


    '''
    table:要插入的表名
    insert_value_dict：要插入的数据{key1:value1,key2:value2,key3:value3}，与update不同
    '''
    def insert(self,table,insert_value_dict):
        self.__connect()
        sql = 'insert into %s%s values %s' % (table,str(tuple(insert_value_dict.keys())).replace("'",''),str(tuple(insert_value_dict.values())))
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.__disconect()
        except:
            return False
        return True


    '''
    table 是一个字符串，代表了要修改的表名
    update_value_dict {用户名:{字段1：值1，字段2：值2}}
    '''
    def update(self,table,update_value_dict):
        self.__connect()
        print update_value_dict
        for outer_key in update_value_dict:
            for inner_key in update_value_dict[outer_key]:
                key= inner_key ;
                value = update_value_dict[outer_key][inner_key]
                sql = 'update %s set %s= "%s" where user_phone="%s"' % (table,key,value,outer_key)
                try:
                    self.cursor.execute(sql)
                    self.conn.commit()
                    self.__disconect()
                except:
                    print '可能有错误 ，亲，好好看看'
                    return False
        return True


    #查询该数据是否存在，目前只支持一个关键字
    def isexist(self,table,isexist_value_dict):
        self.__connect()
        sql = 'select * from %s where %s="%s"' %(table,isexist_value_dict.keys()[0],isexist_value_dict.values()[0])
        print sql
        self.cursor.execute(sql)
        conn_result = self.cursor.fetchall()
        self.__disconect()
        return conn_result


    # def require(self,table,require_value_dict):
    #     self.__connect()
    #     sql= 'select * from %s where '


    def insert_all(self,insert_value_list):
        pass