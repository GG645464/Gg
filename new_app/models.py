# encoding:utf-8
from django.db import models

# Create your models here.


class Grades(models.Model):
    gname = models.TextField(max_length=15)
    gdate = models.DateTimeField(auto_now=True)
    ggirlnum = models.IntegerField(default=0)
    gboynum = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

    class Meta:
        # 数据库中的表名
        db_table = "grades"
        # 排序
        ordering = ['-id']


class StudentManager(models.Manager):
    """修改管理器返回的查询集"""
    def get_queryset(self):
        # 重写get_queryset方法
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    # 1)在修改管理器中写一个创建对象的方法，管理器调用该方法实现创建对象
    def create_student(self, name, age, gender, contend, grade, is_delete=False):
        # 创建stu对象
        stu = self.model()  # type(stu) -->> <object, Students>
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.isDelete = is_delete
        stu.sgrade = grade
        return stu


class Students(models.Model):
    # 自定义模型管理器[当自定义模型管理器后
    # 模型的默认objects管理器就不存在了]
    stuObj = models.Manager()
    stuObj2 = StudentManager()
    sname = models.TextField(max_length=15)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.TextField(max_length=15)
    isDelete = models.BooleanField(default=False)
    # 关联Grades表(一对多，外键写在多)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

    class Meta:
        # 数据中的表名
        db_table = "students"
        # 排序
        ordering = ['id']

    @classmethod
    # 2)在模型中写一个类方法，create_student(cls,....)
    def create_student(cls, name, age, gender, contend, grade, is_delete=False):
        """
            创建对象
            cls代表Students类
        """
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend, isDelete=is_delete, sgrade=grade)
        return stu


from tinymce.models import HTMLField
class Text(models.Model):
    # str = HTMLField(verbose_name=u"这里填写的内容", max_length=256, blank=True)
    str = HTMLField()


