from django.contrib import admin

# Register your models here.
from api.models import BookInfo, PeopleInfo

# 注册模型类
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# 重新运行django
