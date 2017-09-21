# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import  AdminUser
# Create your views here.

def logValid(fun):
    """
    装饰器
    进行session验证，目的如果不通过login直接访问index，
    会因为被检测到不存在session进行登录
    :param fun:
    :return:
    """
    def inner(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return HttpResponseRedirect('/login/')
        return fun(request, *args, **kwargs)
    return inner


def hashpassword(password):
    """
    统一进行hash 加密
    :param password:
    :return:
    """

@logValid
def index(request):
    userList = AdminUser.objects.all()
    userid = request.session['user_id']
    user = AdminUser.objects.get(id=userid)
    return render_to_response('index.html', locals())


def login(request):
    if request.method == "POST" and request.POST:
        phone = request.POST['phone']
        password = request.POST['password']
        try:
            user = AdminUser.objects.get(phone=phone)
        except KeyError:
            return render(request, 'login.html', locals())
        else:
            if user.password == password:
                response = HttpResponseRedirect('/User/index/')
                response.set_cookie('username', user.username, 3600)
                request.session['user_id'] = user.id
                return response
            else:
                return render(request, 'login.html', locals())
    else:
        return render(request, 'login.html', locals())

def logout(request):
    try:
        del request.COOKIES['username']
        del request.session['user_id']
    except:
        pass
    return HttpResponseRedirect('/Usr/login')