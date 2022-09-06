from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def index(request):
    return HttpResponse("bookmanage2")


def eat(request, cid, kid):
    query = request.GET
    res = query.getlist('k')
    print(query)
    print(res)
    return HttpResponse("city:{},kid:{}".format(cid, kid))


def register(request):
    query = request.POST
    print(query)
    return HttpResponse("bookmanage2111")


def jsonw(request):
    body = request.body
    # print(body)
    s = body.decode()
    print(s)
    js = json.loads(s)
    print(js)
    return HttpResponse("json")


def res(request):
    s = {
        "status": 200,
        "name": "yuu",
        "age": 20
    }
    girl_firends = [
        {
            'name': 'rose',
            'address': 'shunyi'
        },
        {
            'name': 'jack',
            'address': 'changping'
        }
    ]
    # data 返回的响应数据 一般是字典类型
    """
    safe = True 是表示 我们的data 是字典数据
    JsonResponse 可以把字典转换为json

    现在给了一个非字典数据， 出了问题 我们自己负责
    """
    # return JsonResponse(data=s)
    # return JsonResponse(data=girl_firends, safe=False)
    d = json.dumps(girl_firends)
    return HttpResponse(d)
