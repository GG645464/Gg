# coding:utf-8

"""
    中间件的作用：每次请求和响应的时候都会调用
    中间件的定义
"""

"""
顺序注册，先执行，后退出(类似栈[先进后出])
输出：
    1111111
    222222
    2222222
    11111111

"""

def simple_middleware(get_response):

    def middleware(request):
        # 请求前
        print('1111111')
        response = get_response(request)
        # 请求后
        print('11111111')
        return response


    return middleware

def simple_middleware2(get_response):
    def middleware2(request):
        # 请求前
        print('222222')
        response = get_response(request)
        # 请求后
        print('2222222')
        return response
    return middleware2

















