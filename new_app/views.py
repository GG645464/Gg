# encoding:utf-8
from django.shortcuts import render, redirect
from .models import Grades, Students
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index1(request):
    # return HttpResponseRedirect('index.html')
    return render(request, "one_app/test.html")


def index(request):
    return HttpResponse("<h1>返回的文字</h1>")
#
#
"""
    2020-10-10
    Django模板
"""
# def detail(request, number1, number2):
#     # return HttpResponse("<h2 style='font-size:40;'>{}-{}</h2>".format(number1, number2))
#     return HttpResponse("<h2 style='font-size:40;'>%s-%s</h2>" % (number1, number2))
#
#
# def grades(request):
#     # 从模板里取数据
#     grades_list = Grades.objects.all()   # 可以获取Grades的所有数据
#     # 将数据传递给模板
#     return render(request, 'one_app/grades.html', {"grades": grades_list})
#
#
# def students(request):
#     students_list = Students.stuObj2.all()
#     return render(request, "one_app/student.html", {"students": students_list})
#
#
# def grades_students(request, num):
#     grades = Grades.objects.get(pk=num)     # 获取指定id的班级
#     student_list = grades.students_set.all()    # 获取指定班级下的所有学生
#     return render(request, 'one_app/student.html', {"students": student_list})
#
#
# def addstudent(request):
#     grade1 = Grades.objects.get(pk=1)
#     stu = Students.create_student("姓名", 45, True, "描述", grade1)
#     stu.save()
#     return HttpResponse("添加对象方法1！")
#
#
# def addstudent2(request):
#     grade1 = Grades.objects.get(pk=2)
#     stu = Students.stuObj2.create_student("姓名56", 78, True, "--", grade1)
#     stu.save()
#     return HttpResponse("添加对象方法2！")
#
#
# def students2(request):
#     students_list = Students.stuObj.all()[0:5]
#     return render(request, "one_app/student.html", {"students": students_list})
#
#
# # 分页显示学生
# def stupage(request, page):
#     page = int(page)
#     students_list = Students.stuObj.all()[(page-1)*5:page*5]
#     return render(request, "one_app/student.html", {"students": students_list})
#
#
# from django.db.models import Max
# # 模糊查询
# def studentsearch(request):
#     # sname__contains这里两个_
#     # students_list = Students.stuObj.filter(sname__contains="姓")
#     # 描述中带有‘姓名1’的数据属于哪个班级
#     # grade = Grades.objects.filter(students__scontend__contains="姓名1")
#     # students_list = Students.stuObj.filter(sname__endswith="1")
#     # students_list = Students.stuObj.filter(pk__in=[2, 4, 5])
#     students_list = Students.stuObj.filter(sage__lt=50)
#     max_age = Students.stuObj2.aggregate(Max('sage'))
#     print(max_age)
#     return render(request, "one_app/student.html", {"students": students_list})
#
#
# from django.db.models import F, Q
# def grades1(request):
#     # 可以使用模型Grades的ggirlnum属性与gboynum属性进行比较
#     # g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
#     # 查询id大于5或者sage小于10的
#     students_list = Students.stuObj.filter(Q(pk__gt=5) | Q(sage__lt=10))
#     return render(request, "one_app/student.html", {"students": students_list})
#

""" 
    2020-10-11
    Django视图
"""

def attribute(request):
    """request请求体对象"""
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribute")


def get1(request):
    # 获取get请求中的参数
    # request.GET.get('键')
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse("{}-{}-{}".format(a, b, c))


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    c1 = c[0]
    c2 = c[1]
    return HttpResponse("{}-{}-{}-{}".format(a1, a2, c1, c2))


def showregist(request):
    return render(request, "one_app/login1.html", {})


def regist(request):
    # request.POST["name"]
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(pwd)
    print(gender)
    print(hobby)
    return HttpResponse("post")


def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    # 异常：unsupported operand type(s) for -: 'bytes' and 'type'
    # print(res.content-type)

    return res


def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie["hello"]+"</h1>")
    # cookie = res.set_cookie("hello", "world")
    return res

# 重定向
from django.http import HttpResponseRedirect
def redirect1(request):
    # return HttpResponseRedirect('/redirect2')
    return redirect("/redirect2")


def redirect2(request):
    return HttpResponse("我是重定向后的视图")


# Session
def main(request):
    print("////")
    # 当第一次没有取到name的值时返回第二个值
    name = request.session.get("name", "游客")
    return render(request, "one_app/main.html", {"name": name})


def login(request):
    print("****")
    return render(request, "one_app/login.html", {})


def showmain(request):
    print("====")
    name = request.POST.get("name")
    # 存储session
    request.session["name"] = name
    # 设置过期时间
    # request.session.set_expiry(10)
    return redirect("/main")


from django.contrib.auth import logout
def quit1(request):
    # 清除session
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect("/main")


def for1(request):
    newlist = Students.stuObj.all()
    oldlist = Students.stuObj.filter(sage__gt=100)
    return render(request, "one_app/student.html", {"students": newlist, "oldlist": oldlist, "str": "zifuchuan",
                                                    "list": ["sun", "sju", "shide"], "code": "<h2>带html标签的内容</h2>"})


def good(request, id):
    return render(request, "one_app/good.html", {"id": id})


def main1(request):
    return render(request, "one_app/index.html")


def detail(request):
    return render(request, "one_app/detail.html")


def postfile(request):
    return render(request, "one_app/postfile.html")


def showinfo(request):
    name = request.POST.get("username")
    pwd = request.POST.get("pwd")
    return render(request, "one_app/showinfo.html", {"name": name, "pwd": pwd})


def upfile(request):
    return render(request, "one_app/upfile.html")

import os
from django.conf import settings
def savefile(request):
    """上传文件类似拷贝文件"""
    # return render(request, "one_app/upfile.html")
    if request.method == "POST":
        f = request.FILES["file"]
        # 文件在服务器端的路径
        filePath = os.path.join(settings.MDEIA_ROOT, f.name)
        with open(filePath, 'wb') as fp:
            # f.chunks()文件分段
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功！")
    else:
        return HttpResponse("上传失败！")


from django.core.paginator import Paginator
def studentpage(request,pageid):
    all_list = Students.stuObj.all()
    paginator = Paginator(all_list, 3)
    page = paginator.page(pageid)
    # print("="*10)
    # # <django.core.paginator.Paginator object at 0x00000212A7AB2DD8>
    # print(page.paginator)
    # # 1
    # print(page.number)
    # # <bound method Sequence.count of <Page 1 of 4>>
    # print(page.count)
    # # <QuerySet [<Students: sfasd>, <Students: 11>, <Students: 33>]>
    # print(page.object_list)
    # # <bound method Sequence.index of <Page 1 of 4>>
    # print(page.index)
    return render(request, "one_app/studentpage.html", {"students": page})


def ajaxstudents(request):
    return render(request, "one_app/ajaxstudents.html")


from django.http import JsonResponse
def studentsinfo(request):
    # Students.stuObj.values()返回字典结构
    stus = Students.stuObj.all()
    stu_list = []
    for stu in stus:
        stu_list.append([stu.sname, stu.sage])
    return JsonResponse({"data": stu_list})


def edit(request):
    return render(request, "one_app/edit.html")


def saveedit(request):
    if request.method == "POST":
        get_str = request.POST.get("str")
        return HttpResponse(get_str)
    else:
        pass
        # return redirect("saveedit/")

