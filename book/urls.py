# coding:utf-8
from django.contrib import admin
from django.conf.urls import url
from . import views
# from book.views import *
app_name = "book"
# urlpatterns = [
#     url('^$',views.redirect_index,name='redirect'),
#     url('^index/$',views.index),
# ]
urlpatterns = [
    url(r'^redirect/$',views.redirect_index,name='redirect'),
    url(r'^redirect1/$',views.redirect_index1,name='redirect1'),
    url(r'^index/$',views.index),
    url(r'^myindex/$',views.myindex),
    url(r'^index1/$',views.index1,name='index1'),
    # url(r'^(\d+)/(\d+)$',views.detail),
    # 关键字参数
    url(r'^(?P<category_id>\d+)/(?P<book_id>\d+)$',views.detail),
    url(r'^cookie/$',views.set_cookie,name='cookie'),
    url(r'^get_cookie/$',views.get_cookie),
    url(r'^login/$',views.BookView.as_view()),
    url(r'center/$',views.CenterView.as_view()),
    url(r'^home/$',views.HomeView.as_view()),

]





















