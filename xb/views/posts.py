# coding= utf-8
# from view.view_posts import *
from django.http import HttpResponse
import datetime
import json
from xb.methods.posts_action import AppPosts
from bson.objectid import ObjectId
from xb.methods import convert_func

def add(request):
    POST = request.POST
    print POST
    user = POST['user']
    title = POST['title']
    content = POST['content']
    print content
    time = str(datetime.datetime.now())[:-7]
    mp = AppPosts()

    mp.add(user=user, title=title, content=content, time=time, comment={})
    return HttpResponse(json.dumps({'1': '2'}), content_type='application/text')


def addcomment(request):
    POST = request.POST
    ap = AppPosts()
    ap.addcomment(convert_func(POST))
    # print dict(POST)
    # user = POST['user']
    # content = POST['content']
    # time = POST['time']
    # oid = POST['oid']
    # print POST
    # time = str(datetime.datetime.now())[:-7]
    # mp = mongo_posts()
    # mp.addcomment(user=user,content=content,oid=oid,time=time)
    return HttpResponse(json.dumps({'1': '2'}), content_type='application/text')

