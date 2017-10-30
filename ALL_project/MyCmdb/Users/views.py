# coding=utf-8
import hashlib
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from forms import AdminUserForm
from PIL import Image
from models import Users
# Create your views here.

def loginValid(fun):
    def inner(request, *args, **keywords):
        #id = request.COOKIES.get('userid')
        #name = request.COOKIES.get('username')
        phone = request.session.get('phone')
        if not phone:
            return HttpResponseRedirect('/login/')
        return fun(request, *args, **keywords)
    return inner


def hashstr(string):
    """
    hash加密字符串
    :param string:
    :return:
    """
    md5str = hashlib.md5()
    md5str.update(string)
    result = md5str.hexdigest()
    return result


def phoneValid(phone):
    """
    当用户提交手机号，验证手机号是否注册，如果有，返回用户信息
    :param string:
    :return:
    """
    try:
        u = Users.objects.get(phone=phone)
    except:
        result = {'status': True, 'data': None}
    else:
        result = {'status': False, 'data': u}
    finally:
        return result


def register_phone(request):
    """
    配合ajax，在前端register页面上验证手机号码是否重复
    :param request:
    :return:
    """
    if request.method == 'GET' and request.GET:
        phone = request.GET['phone']
        valid = phoneValid(phone)
        if valid['status']:
            result = {'status': 'success'}
        else:
            result = {'status': 'error'}
    else:
        result = {'status': 'phone is not found'}
    return JsonResponse(result)

@loginValid
def register(request):
    """
    注册用户
    :param request:
    :return:
    """
    if request.method == 'POST' and request.POST:
        img = request.FILES
        data = request.POST
        photo = img['photo']
        photo_name = str(photo)
        img = Image.open(photo)
        img.save('static/img/uploadImg/'+photo_name)

        u = Users()
        u.phone = data['phone']
        u.user = data['user']
        u.password = hashstr(data['password'])
        u.email = data['email']
        u.isadmin = int(data['isadmin'])
        u.photo = photo_name
        u.save()
    userid = request.COOKIES.get('user_id')
    try:
        user = Users.objects.get(id=userid)
    except:
        return HttpResponseRedirect('/login/')
    form = AdminUserForm()
    return render(request, 'register.html', locals())