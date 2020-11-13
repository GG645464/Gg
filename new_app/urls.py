# coding:utf-8
from django.conf.urls import url
from . import views

app_name = "one1app"

urlpatterns = [
    url(r'^$', views.index1, name="index"),
    url(r'^index.html', views.index, name="index"),
    # url(r'^(\d+)/(\d+)$', views.detail, name='detail'),
    # url(r'^grades/$', views.grades, name='grades'),
    # url(r'^students/$', views.students, name='students'),
    # url(r'^students2/$', views.students2, name='students2'),
    # url(r'^stu/(\d+)/$', views.stupage, name='stupage'),
    # url(r'^studentsearch/$', views.studentsearch, name='studentsearch'),
    # url(r'^grades/(\d+)$', views.grades_students, name='grades_students'),
    # url(r'^addstudent/$', views.addstudent, name="add_student"),
    # url(r'^addstudent2/$', views.addstudent2, name="add_student2"),
    # url(r'^grades1/$', views.grades1, name="grades1"),
    url(r'^attribute', views.attribute, name="attribute"),
    url(r'^get1', views.get1),
    url(r'^get2', views.get2),
    url(r'^regist/$', views.regist),
    url(r'^showregist/$', views.showregist),
    url(r'^showresponse', views.showresponse),
    url(r'^cookietest', views.cookietest),
    url(r'^redirect1', views.redirect1),
    url(r'^redirect2', views.redirect2),
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain$', views.showmain),
    url(r'^quit/$', views.quit1),
    url(r'^for1/$', views.for1),
    url(r'^good/(\d+)/$', views.good, name="good"),
    url(r'^main1/$', views.main1),
    url(r'^detail/$', views.detail),
    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo),
    url(r'^upfile/$', views.upfile),
    url(r'^savefile/$', views.savefile),
    url(r'^studentpage/(\d+)/$', views.studentpage),
    url(r'^ajaxstudents/$', views.ajaxstudents),
    url(r"^studentsinfo/$", views.studentsinfo),
    url(r"^edit/$", views.edit),
    url(r"^saveedit/$", views.saveedit, name="saveedit"),

]






















