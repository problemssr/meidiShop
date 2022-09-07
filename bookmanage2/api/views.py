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


def setcook(request):
    usr = request.GET.get('usrname')
    response = HttpResponse('set_cookie')
    response.set_cookie('name', usr)
    return response


def getcook(request):
    name = request.COOKIES.get("name")
    # print()
    return HttpResponse('get_cookie ' + name)


def set_session(request):
    username = request.GET.get('username')
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    # request.session.clear()
    # request.session.flush()
    request.session.set_expiry(3600)
    return HttpResponse("set_session")


def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    content = "{}, {}".format(user_id, username)
    return HttpResponse("get_session " + content)


###############################类视图###################################
"""
类视图的定义

class 类视图名字（View）:

    def get(self,request):

        return HttpResponse('xxx')

    def http_method_lower(self,request):

        return HttpResponse('xxx')

1. 继承自View
2. 类视图中的方法 是采用 http方法小写来区分不同的请求方式
"""
from django.views import View


class LoginView(View):
    def get(self, request):
        return HttpResponse('get aaa')

    def post(self, request):
        return HttpResponse("post aa")


from django.contrib.auth.mixins import LoginRequiredMixin


class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        isLogin = False
        if not isLogin:
            return HttpResponse("未登录")
        return HttpResponse("get 登录")

    def post(self, request):
        return HttpResponse("post 登录")


def vue_test(request):
    return render(request, 'index.html')


def v_model(request):
    return render(request, 'model.html')


def todo(request):
    return render(request, 'todo.html')
