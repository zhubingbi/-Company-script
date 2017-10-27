# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import Servers
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt   # 接口避免CSRFtoken验证
def saveServer(request):
    result = {'status': '', 'data': ''}
    if request.method == 'POST' and request.POST:
        mac = request.POST['mac']
        try:
            server = Servers.objects.get(mac=mac)
        except:
            server = Servers()
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.mac = request.POST['mac']
            server.sys = request.POST['sys']
            server.memory = request.POST['memory']
            server.disk = request.POST['disk']
        else:
            server.hostname = request.POST['name']
            server.ip = request.POST['ip']
            server.sys = request.POST['sys']
            server.memory = request.POST['memory']
            server.disk = request.POST['disk']
        finally:
            server.save()
        result['status'] = 'success'
        result['data'] = 'save success'
    else:
        result['status'] = 'error'
        result['data'] = 'method must be post and not null'
    return JsonResponse(result)