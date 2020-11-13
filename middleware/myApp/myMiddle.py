# coding:utf-8
from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    def process_request(self, request):
        """
        在执行视图之前被调用(分配url匹配视图之前)，
        每个请求上都会调用，返回None或者HttpResonse对象
        """
        # print("get参数为：", request.GET.get("a"))
        pass



















