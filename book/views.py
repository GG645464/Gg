# coding:utf-8
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,JsonResponse
from book.models import BookInfo,PeopleInfo
from django.db.models import F,Q
import datetime
import json
# Create your views here.


def index1(request):
    path = reverse('book:redirect1')
    print(path+" ="*10)
    return redirect(path)
def index(request):
    # return render()
    return HttpResponse("index")

def test(request):
    """1.新增数据的两种方法
    BookInfo(
            name='aa',
            pub_date='2020-11-07',

        )

        BookInfo.objects.create(
            name='bb',
            pub_date='2020-11-08',

        )

        2.更新数据的两种方式
            1.先查新数据
                select * from bookinfo where id=1
                book = BookInfo.objects.get(id=1)
            2.直接修改数据
                BookInfo.objects.filter(name='aa').update(
                readcount = 10,
                commentcount = 20,

        )

        3.删除数据的两种方式
            1.
                book1 = BookInfo.objects.get(name='aa')
                book1.delete()
            2.BookInfo.objects.filter(name='bb').delete()

        4.select * from bookinfo where 条件语句
        想当于where查询
        filter：筛选/过滤  返回n个结果
        get：过滤单一结果    返回一个结果
        exclude：排除掉符合条件剩下的结果 相当于not
    语法形式：
        以filter(字段名__运算符=值)

    """
    """======================================================"""
    # 1.需要调用save方法
    # book = BookInfo(
    #     name = 'aa',
    #     pub_date = '2020-11-07',
    #
    # )
    #
    # book.save()

    # 2.直接创建
    # BookInfo.objects.create(
    #     name = 'bb',
    #     pub_date = '2020-11-08',
    #
    # )
    """=========================================================="""
    # 1.查询修改更新
    # book1 = BookInfo.objects.get(name='aa')
    # book1.readcount = 1
    # book1.save()

    # 2.直接更新
    # BookInfo.objects.filter(name='aa').update(
    #     readcount = 10,
    #     commentcount = 20,
    #
    # )
    """============================================================="""
    # 1.查询删除
    # book1 = BookInfo.objects.get(name='aa')
    # book1.delete()
    # 2.直接删除
    # BookInfo.objects.filter(name='bb').delete()
    """============================================================="""
    # 查询
    # 1.指定查询
    # book = BookInfo.objects.get(id=1) # 返回：<BookInfo: BookInfo object (1)>
    # 2.查询全部
    # book_list = BookInfo.objects.all()    # 返回：<QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (2)>, <BookInfo: BookInfo object (3)>, <BookInfo: BookInfo object (4)>]>
    # 3.查询总数
    # count = BookInfo.objects.count()      # 返回：4
    # 4.查询编号为1的图书(exact->精确的)
    BookInfo.objects.get(id__exact=1)   # 返回：<BookInfo: BookInfo object (1)>
    BookInfo.objects.filter(id__exact=1)    # 返回：<QuerySet [<BookInfo: BookInfo object (1)>]>
    # 5.查询书名包含'晓'的图书
    BookInfo.objects.filter(name__contains='晓') # 返回：<QuerySet [<BookInfo: BookInfo object (2)>]>
    # 6.查询书名以'你'结尾的图书
    BookInfo.objects.filter(name__endswith='你') # 返回：<QuerySet [<BookInfo: BookInfo object (4)>]>
    # 7.查询书名为空的图书
    BookInfo.objects.filter(name__isnull=True) # 返回：<QuerySet []>
    # 8.查询编号为1或3或5的图书
    BookInfo.objects.filter(id__in=[1,3,5]) # 返回：<QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (3)>]>
    # 9.查询编号大于3的图书(gt大于,gte大于等于,lt小于，lte小于等于)
    BookInfo.objects.filter(id__gt=3)   # 返回：<QuerySet [<BookInfo: BookInfo object (4)>]>
    # 10.查询书籍id不为3的图书
    BookInfo.objects.exclude(id=3) # 返回：<QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (2)>, <BookInfo: BookInfo object (4)>]>
    # 11.查询2020年发表的图书
    BookInfo.objects.filter(pub_date__year='2020') # 返回<QuerySet [<BookInfo: BookInfo object (2)>, <BookInfo: BookInfo object (4)>]>
    # 12.查询1990年11月7日前发表的图书
    BookInfo.objects.filter(pub_date__lt='2020-11-7') # 返回：<QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (3)>]>
    """================================================="""
    # F对象：用于两个字段(属性)之间比较
    # 语法形式：filter(字段名__运算符=F('字段名'))
    # 查询阅读量大于等于评论量的图书
    BookInfo.objects.filter(readcount__gte=F('commentcount')) # 返回:<QuerySet [<BookInfo: BookInfo object (2)>]>
    # 查询阅读量大于等于评论量的图书2倍
    BookInfo.objects.filter(readcount__gte=F('commentcount')*2) # 返回：<QuerySet []>
    """=================================================="""
    # Q对象
    # 语法格式：Q(字段名__运算符=值)    或：Q()|Q()   且Q()&Q() not:~Q()
    # 查询id大于2并且阅读量大于20的书籍
    BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20) # 返回：<QuerySet [<BookInfo: BookInfo object (4)>]>
    BookInfo.objects.filter(id__gt=2,readcount__gt=20) # 返回：<QuerySet [<BookInfo: BookInfo object (4)>]>
    # 查询id大于2或者阅读量大于20的书籍
    BookInfo.objects.filter(Q(id__gt=2)|Q(readcount__gt=20)) # 返回：<QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (3)>, <BookInfo: BookInfo object (4)>]>
    # 查询书籍id不为3
    BookInfo.objects.filter(~Q(id=3))   # 返回：<QuerySet [<BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (2)>, <BookInfo: BookInfo object (4)>]>
    """=================================================="""
    # 聚合函数 Sum，Max，Min，Avg，Count
    # 聚合函数需要使用 aggregate
    # 语法格式：aggragte(Xxx('字段'))
    from django.db.models import Sum,Max
    # 当前数据的阅读量
    BookInfo.objects.aggregate(Sum('readcount')) # 返回：{'readcount__sum': 77} -> count.readcount__sum
    """=================================================="""
    # 排序
    # 默认升序排列
    BookInfo.objects.all().order_by("readcount") # 返回：<QuerySet [<BookInfo: BookInfo object (3)>, <BookInfo: BookInfo object (2)>, <BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (4)>]>

    # 降序
    BookInfo.objects.all().order_by("-readcount") # 返回：<QuerySet [<BookInfo: BookInfo object (4)>, <BookInfo: BookInfo object (1)>, <BookInfo: BookInfo object (2)>, <BookInfo: BookInfo object (3)>]>
    """=================================================="""
    # TODO 关联查询
    # 书籍和人物的关系是1：n
    """
        已知主表数据，查询从表数据
        主表模型对象.关联模型类名小写_set.all()
    """
    # 1.查询书籍为1的所有人物信息 书籍1从1查多用set.all()
    book = BookInfo.objects.get(id=1)
    book.peopleinfo_set.all() # 返回：<QuerySet [<PeopleInfo: 是>]>
    """从表模型对象.外键"""
    # 2.查询人物为1的书籍信息 人物n从多查1用外键
    people = PeopleInfo.objects.get(id=1) # 返回：<PeopleInfo: 小红>
    # 在通过外键查询到people.bookid书籍信息(people.bookid.readcount)
    """=================================================="""
    # 语法格式：filter(关联模型类名小写__字段__运算符=值)
    # 1.查询图书，要求图书人物为'小红'
    BookInfo.objects.filter(peopleinfo__name='小红') # 返回：<QuerySet [<BookInfo: BookInfo object (1)>]>
    # 2.查询图书，要求图书中人物描述包含‘2’
    BookInfo.objects.filter(peopleinfo__description__contains='2')  # 返回：<QuerySet [<BookInfo: BookInfo object (1)>]>
    # 语法格式：filter(外键__字段__运算符=值)
    # 3.查询书名为的"晓晓"的所有人物
    PeopleInfo.objects.filter(bookid__name="晓晓") # 返回：<QuerySet [<PeopleInfo: ii>]>
    # 4.查询图书阅读量小于30的所有人物
    PeopleInfo.objects.filter(bookid__readcount__lt=30) # 返回:<QuerySet [<PeopleInfo: 小红>, <PeopleInfo: 小明>, <PeopleInfo: ii>]>
    """=================================================="""
    return HttpResponse("<h2>"+ str(1)+"</h2>")


def redirect_index1(request):

    return HttpResponse("index1")

def detail(request,book_id,category_id):
    print(book_id,category_id)
    params = request.GET
    print(params) # <QueryDict: {'name': ['123'], 'pwd': ['g123']}>
    print(request.GET.getlist('name')) # ['123']
    print(request.GET.get('name')) # 123
    """
        json.dumps  将字典转化成JSON形式的字符串
        json.loads  将JSON形式的字符串转化成字典
    """
    return HttpResponse('detail')

def redirect_index(request):
    print("*"*20)
    return redirect("/index")

from django.core.paginator import Paginator
def myindex(request):
    """
    分页
    :param request:
    :return:
    """
    books = BookInfo.objects.all()
    p = Paginator(books,2)
    books_page = p.page(1)
    return render(request,"book/index.html",{"books_page":books_page})

def set_cookie(request):

    name = request.GET.get('name')
    response = HttpResponse('cookie')
    request.session['user_id'] = 465
    response.set_cookie("name",name,max_age=20)

    return response

def get_cookie(request):
    cookies = request.COOKIES

    name = cookies.get('name')

    return HttpResponse("get_cookie")

"""
    面向对象
        类视图
            1.定义类视图
                1)继承自 View (from django.views import View)
                2)不同的请求方式，有不同的业务逻辑
                3)类视图的方法的第二个参数 必须的请求实例对象
                    类视图的方法，必须要有返回值，返回值是HttpResponse对象
            2.类视图的url引导
"""
def login(request):
    if request.method == 'GET':
        return render(request)
    else:
        return redirect('首页')

from django.views import View

class HomeView(View):
    def get(self,request):
        name = request.GET.get('name')
        context = {
            'name':name,
            "age":10,
            'birthday':'2020-11-04',
            "friends":['tom','jack','rose'],
            'money':{
                '2019':12000,
                '2020':18000,
                '2021':25000,

            }
        }
        return render(request,'book/index.html',context=context)

"""
    个人中心首页
    GET方式展示个人中心
    POST方式实现个人中心信息的修改
    定义类视图
"""
# django类视图->继承规则
# class CenterView(BookView,View):
class CenterView(View):
    def get(self,request):
        return HttpResponse("个人中心展示")

    def post(self,request):
        return HttpResponse("个人中心修改")


class BookView(View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')

class Person(object):
    # cls -->Person 类
    @classmethod
    def say(cls):
        pass

    # self -> 实例对象
    def eat(self):
        pass

    @staticmethod
    def run():
        pass

# Person.say()
# p = Person()
# p.say()

class LoginView(View):
    def get(self,request):
        return render(request,'book/login.html')

    def post(self,request):
        pass


class ReceiveView(View):
    def get(self,request):
        # 接收参数
        info = request.GET
        username = info.get("username")
        password = info.get("password")

        return JsonResponse({"info":{"username":username,"password":password}})

    def post(self,request):
        # 接收参数
        # info = request.POST
        # Json数据在body中获取，body数据需要decode
        info = json.loads(request.body.decode())

        username = info.get("username")
        password = info.get("password")

        return JsonResponse({"info":{"username":username,"password":password}})


