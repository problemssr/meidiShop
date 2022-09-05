from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(路由，视图函数名)
    # path('index/', views.index),
    # path('blog/',include('api.urls'))
    path('', include('api.urls'))
]
