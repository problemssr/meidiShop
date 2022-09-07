from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        username = request.COOKIES.get("name")
        if username is None:
            print("没有用户信息")
        else:
            print("有用户信息")
        print("请求111")

    def process_response(self, request, response):
        print("响应111")
        return response


class TestMiddleWare2(MiddlewareMixin):
    def process_request(self, request):
        username = request.COOKIES.get("name")
        if username is None:
            print("没有用户信息")
        else:
            print("有用户信息")
        print("请求222")

    def process_response(self, request, response):
        print("响应222")
        return response
