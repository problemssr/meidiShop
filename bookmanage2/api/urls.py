from django.urls import path
from api import views
from django.urls import register_converter


class MobileConverter:
    """自定义路由转换器：匹配手机号"""
    # 匹配手机号码的正则
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        # 将匹配结果传递到视图内部时使用
        return int(value)

    def to_url(self, value):
        # 将匹配结果用于反向解析传值时使用
        return str(value)


register_converter(MobileConverter, 'mobile')

urlpatterns = [
    path('index/', views.index),
    path('<int:cid>/<mobile:kid>/', views.eat),
    path('register/', views.register),
    path('jsonw/', views.jsonw),
    path('res/', views.res),
    path('setcook/', views.setcook),
    path('getcook/', views.getcook),
    path('set_session/', views.set_session),
    path('get_session/', views.get_session),
    path('login/', views.LoginView.as_view()),
    path('order/', views.OrderView.as_view()),
    path('vue_test/', views.vue_test),
    path('v_model/', views.v_model),
    path('todo/', views.todo),

]
