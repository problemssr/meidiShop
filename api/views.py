from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python函数
视图函数有2个要求：
    1. 视图函数的第一个参数就是接收请求。这个请求其实就是 HttpRequest的类对象
    2. 必须返回一个响应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):
    # return HttpResponse('ok')
    context = {
        'name': '双十一冲冲冲'
    }
    return render(request, 'index.html', context)
