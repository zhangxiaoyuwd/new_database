from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    """
    访问首页
    :param request:
    :return:
    """
    return HttpResponse("index")

def login(requset):
    """
    访问登录界面
    :param requset:
    :return:
    """
    return redirect("/index")
