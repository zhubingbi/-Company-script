# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Us
import hashlib

#def index(request):
    #return render_to_response('index.html', locals())


def tak_md5(content):
    hash = hashlib.md5()
    # 创建一个hash加密实例
    hash.update(content)
    # 进行加密
    result = hash.hexdigest()
    # 得到加密结果
    return result


def index(request):
    all_user = Us.objects.all() # 查询
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        password = tak_md5(password)
        if username and password:
            user = Us()
            user.user = username
            user.password = password
            user.save()

    return render(request, 'index.html', locals())
# Create your views here.

from form import Register
def loveRegister(request):
    if request.method == 'POST' and request.POST:
        register = Register(request.POST) # 对form表单提交的数据进行验证
        if register.is_valid(): #判断验证是否通过
            data = register.cleaned_data
            print ('save Data')
        else:
            error = register.errors
    else:
        register = Register()
    return render(request,'register.html', locals())

def ajaxTest(request):
    return render(request, 'ajaxTest.html')
