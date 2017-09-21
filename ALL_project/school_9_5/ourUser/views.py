# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response


def logValid(fun):
    """
    装饰器
    进行session验证，目的如果不通过login直接访问index，
    会因为被检测到不存在session进行登录
    :param fun:
    :return:
    """
    def inner(request, *args, **kwargs):
        if not request.session.get('name'):
            return HttpResponseRedirect('/login/')
        return fun(*args, **kwargs)
    return inner

def hashpassword(password):
    """
    统一进行hash 加密
    :param password:
    :return:
    """

@logValid
def register(request):
    pass

@logValid
def login(request):
    pass

@logValid
def userindex(request):
    pass
