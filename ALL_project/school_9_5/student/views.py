# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from form import StudentForm
from models import Student
from django.shortcuts import HttpResponseRedirect

def register(request):
    if request.method == "POST" and request.POST:
        # 判断提交的数据为post, 并且post有数据
        sForm = StudentForm(request.POST)
        # 把post数据交给form表单验证
        if sForm.is_valid():
            # 判断form 表单是否正确
            clean_data = sForm.cleaned_data
            # 获取验证过的数据
            s = Student()
            # 实例化 import 的数据库model
            s.name = clean_data['name']
            s.gender = clean_data['gender']
            s.age = clean_data['age']
            s.birthday = clean_data['birthday']
            s.grade = clean_data['grade']
            s.subject = clean_data['subject']
            s.city = clean_data['city']
            s.save()
            return HttpResponseRedirect('/list/1', locals())
            # 重定向url
        else:
            pass
            # 前台验证
    else:
        sForm = StudentForm()
    return render(request, 'register.html', locals())
# Create your views here.

def valide_name(request):
    if request.method == 'GET' and request.GET:
        name = request.GET['name']
        result = {}
        try:
            student = Student.objects.get(name = name)
            result['statue'] = 'error'
        except:
            result['statue'] = 'success'
    return JsonResponse(result)

#def list(request, page, pagesize=10):
#    # 前端分页
#    # all_student = Student.objects.all()[0:10]
#    page = int(page)
#    start = (page-1)*pagesize
#    end = page*pagesize
#    page_student = Student.objects.all()[start:end]
#    if page == 1:
#        uper = 1
#    else:
#        uper = page-1
#    next = page+1
#    return render_to_response("list.html", locals())

def list(request):
    return render_to_response('list_v2.html', locals())

def listData(request):
    """
    当请求该函数，返回
    指定条数据，数据的总条数，up, down
    __gt 大于
    __gte 大等于
    __lt 小于
    __lte 小等于
    __range 范围
    :param request:
    :return:
    """
    if request.method == 'GET' and request.GET:
        page = int(request.GET['page'])
        pagesize = int(request.GET['pagesize'])
        start = (page-1)*pagesize
        end = page*pagesize

        total_length = len(Student.objects.all())
        total_range = range(1, total_length/pagesize+1)

        student_list = Student.objects.filter(id__range=(start, end))
        result = []

        for student in student_list:
            student_dict = {}
            student_dict['id'] = student.id
            student_dict['name'] = student.name
            student_dict['age'] = student.age
            student_dict['gender'] = student.gender
            student_dict['subject'] = student.subject
            result.append(student_dict)
        if page != 1:
            p = page -1
        else:
            p = page
        allResult = {
            'total':total_range,
            'data':result,
            'up':p,
            'down':page+1
        }
    else:
        allResult = {
            'total': 0,
            'data': [],
            'up': 0,
            'down': 0
        }
    return JsonResponse(allResult)

def index(request):
    name = request.COOKIES['name']
    session = request.session['name']
    sForm = StudentForm()
    return render_to_response('index.html', locals())

def testcookie(request):
    response = render_to_response('testCookie.html', locals())
    response.set_cookie('name', 'while', 3600)
    # 键，值，最大时间，expire 失效时间， path cookie 生效的范围，Doamin 生效的站点
    return response

def testSession(request):
    request.session['name'] = 'zhubingbi'
    return render_to_response('testSession.html', locals())
