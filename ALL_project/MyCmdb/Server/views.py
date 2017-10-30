# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import Servers
from django.views.decorators.csrf import csrf_exempt
from MyCmdb.views import loginValid
from Users.models import Users


@csrf_exempt   # 接口避免CSRFtoken验证
def saveServer(request):
    """
    接口提交服务器信息
    :param request:
    :return:
    """
    result = {'status': '', 'data': ''}
    if request.method == 'POST' and request.POST:
        try:
            mac = request.POST['mac']
            server = Servers.objects.get(mac=mac)
        except:
            # 如果是新mac地址，添加新的.
            server = Servers()
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.mac = request.POST['mac']
            server.sys = request.POST['sys']
            server.memory = request.POST['memory']
            server.disk = request.POST['disk']
            server.cpu = request.POST['cpu']
        else:
            # 存在mac地址，就修改原有的.
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.sys = request.POST['sys']
            server.memory = request.POST['memory']
            server.disk = request.POST['disk']
            server.cpu = request.POST['cpu']
        finally:
            server.save()
        result['status'] = 'success'
        result['data'] = 'save success'
    else:
        result['status'] = 'error'
        result['data'] = 'method must be post and not null'
    return JsonResponse(result)


@loginValid
def serverlist(request, number=5):
    number = int(number)
    userid = request.COOKIES.get('user_id')
    user = Users.objects.get(id=userid)
    if request.method == 'GET' and request.GET:
        p = int(request.GET['page'])
    else:
        p = 1
    page_up = (p-1)*number
    page_down = p*number
    all_server = Servers.objects.all()
    serverList = all_server[page_up:page_down]
    total = len(all_server)
    page = total/float(number)
    if int(page) != page:
        page = int(page) + 1
    else:
        page = int(page)
    page_size = range(1, page+1)
    return render_to_response('serverlist.html', locals())