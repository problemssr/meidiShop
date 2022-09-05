from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)


# 人物 先复制过来。后期将原理
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
