#coding:utf-8

from hashlib import md5
from random import randint
from xb.methods.mysql_class import MysqlConnect
from xb.settings import DEFAULT_PHOTO
from datetime import datetime

#这个模块是用来用户 登陆的.
class AppLogin(object):
    def __init__(self,user_phone,user_password):
        self.user_phone = user_phone
        self.user_password =user_password
        self.conn= MysqlConnect()
        self.status=''
        self.code=''
        self.ret=''

    def login(self):
        self.__check_number()

    def __check_number(self):
        user_phone = self.user_phone
        user_password = md5(self.user_password+self.user_phone+'shyn').hexdigest()
        user_detail_tuple = self.conn.isexist('user_info',{'user_phone':user_phone})
        if user_detail_tuple:
            self.__check_password(user_detail_tuple[0],user_password)
        else:
            self.status='1'
            self.code='401'



    def __check_password(self,user_detail_tuple,user_password1):
        if user_detail_tuple[3] == user_password1:
            self.status='0'
            self.ret={'user_photo':user_detail_tuple[4],'user_token':self.__set_token()}
        else:
            self.status='1'
            self.code='401'



    def __set_token(self):
        user_token =  md5(self.user_phone + str(randint(100000,200000))).hexdigest()
        update_value_dict = {self.user_phone:{'user_token':user_token}}
        self.conn.update('user_info',update_value_dict)
        return user_token



class AppLogout(object):
    def __init__(self,user_id,user_password):
        self.user_id = user_id;
        self.user_password = md5(user_password);


    def user_logout(self):
        pass


    def __destroyUserToken(self):
        pass


    def __destroyAllToken(self):
        pass



class AppRegister(object):
    def __init__(self,user_phone,user_password):
        self.user_phone = user_phone
        self.user_password = user_password
        self.conn= MysqlConnect()
        self.status=''
        self.code=''
        self.ret=''


    def __check_number(self):
        user_phone=self.user_phone
        result= self.conn.isexist('user_info',{'user_phone':user_phone})
        return not result


    def register(self):
        if self.__check_number():
            if self.__insert_mysql():
                # self.status='1050'
                self.code= '201'
                self.status='0'
            else:
                self.status='1'
                self.code='500'
        else:
            self.status='1'
            self.code='422'
            # print '1003'


    def __insert_mysql(self):
        user_id= md5(self.user_phone+'shyn').hexdigest()
        user_phone= str(self.user_phone)
        user_name = (str(self.user_phone[:3])+md5(user_phone).hexdigest())[:10]
        user_password = md5(self.user_password+self.user_phone+'shyn').hexdigest()
        user_photo = DEFAULT_PHOTO
        user_create = str(datetime.now())[:19]
        insert_value_dict={'user_id':user_id,'user_phone':user_phone,'user_name':user_name,'user_password':user_password,'user_photo':user_photo,'user_create':user_create}
        return self.conn.insert('user_info',insert_value_dict)





