# encoding:utf-8
from django.db import models

# Create your models here.
"""
1.ORM
    表 ->> 类
    字段 ->> 属性
2.模型类需要继承models.Model
    null    是否为空
    unique  唯一
    default 设置默认值
    verbose_name    主要是admin后台显示
3.模型类会自动为我们添加一个主键
书籍表
    id,name,pub_date,readcount,commentcount,is_delete
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 修改表名
    class Meta:
        db_table = "bookinfo"

class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')
    )
    name = models.CharField(max_length=20,verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    description = models.CharField(max_length=200,null=True,verbose_name='描述')
    bookid = models.ForeignKey(BookInfo,on_delete=models.CASCADE) # cascade级联

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'
    def __str__(self):
        return self.name

