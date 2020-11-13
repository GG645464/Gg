# encoding:utf-8
from django.contrib import admin

# Register your models here.
from .models import Grades, Students, Text


# 注册
class StudentInfo(admin.TabularInline):     # 更好看
    # class StudentInfo(admin.StackedInline):
    model = Students
    extra = 2


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    # 需要先定义StudentInfo类
    inlines = [StudentInfo]
    """列表页属性"""
    # 显示属性list_display
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    # 过滤器
    list_filter = ['gname']
    # 搜索框
    search_fields = ['gname']
    # 分页
    list_per_page = 2

    # ==============分隔=================
    # 添加、修改页属性
    """PS： fields 和 fieldsets不能同时使用"""
    # fields = ['gname', 'gdate', 'ggirlnum', 'gboynum']
    # 给属性分组
    fieldsets = [
        ("base", {"fields": ['gname', 'gdate']}),
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("other", {"fields": ['isDelete']}),
    ]


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 修改字段显示值
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    def name(self):
        return self.sname

    # 修改表头字段显示值
    gender.short_description = "性别"
    name.short_description = "姓名"
    list_display = ['pk', name, gender, 'sage', 'scontend', 'sgrade', 'isDelete']

    actions_on_bottom = True
    actions_on_top = False


admin.site.register(Text)
# admin.site.register(Grades, GradesAdmin)
# admin.site.register(Grades)
# admin.site.register(Students, StudentsAdmin)

