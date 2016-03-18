#coding=utf-8
from pymongo import MongoClient
# from xb.settings.set_mongo_xiaobai import set_mongo_xiaobai,conf_mongo_add_timestamp
from bson.objectid import ObjectId
from xb.settings import MONGO_XB
from datetime import datetime

#该模块是关于APP端帖子的，应该有用的
class AppPosts(object):
    def __init__(self):
        self.db = self.__connect()

    def __connect(self):
        client = MongoClient(MONGO_XB)
        db = client['xiaobai']
        return db


    def search(self):
        pass


    def delete(self):
        pass


    def add(self,*args,**kwargs):
        print kwargs
        mong_posts = self.db['posts']
        mong_posts.insert_one(kwargs)


    def addcomment(self,comm_dict):
        user = comm_dict['user']
        oid = comm_dict['oid']
        del comm_dict['user']
        del comm_dict['oid']
        comm_dict['time']=str(datetime.now())
        
        mongo_posts= self.mongo_db['posts']
        mongo_comment = self.mongo_db['comment']
        mc = self.mc

    def delcomment(self):
        pass


