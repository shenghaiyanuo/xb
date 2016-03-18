#coding:utf-8
from django.http import HttpResponse
from xb.methods.user_action import AppLogin,AppLogout,AppRegister
from hashlib import md5
from xb.methods.xblog_func import  log_user
import json

# def deco(func):
#     def __deco(request):
#         print request.POST
#         ret = func(request)
#         print ret
#         return ret
#     return __deco

@log_user
def login(request):
    POST = request.POST
    # print POST
    user_phone=POST['user_phone']
    user_password=POST['user_password']
    user = AppLogin(user_phone,user_password)
    user.login()
    # print HttpResponse(json.dumps({'status':user.status,'code':user.code,'ret':user.ret}), content_type="application/json")
    return HttpResponse(json.dumps({'status':user.status,'code':user.code,'ret':user.ret}), content_type="application/json")


@log_user
def register(request):
    POST= request.POST
    user_phone=POST['user_phone']
    user_password=POST['user_password']
    user = AppRegister(user_phone,user_password)
    user.register()
    return HttpResponse(json.dumps({'status':user.status,'code':user.code,'ret':user.ret}), content_type="application/json")


#
# def logout(request):
#     POST = request.POST
#     user_phone=POST['user_phone']

