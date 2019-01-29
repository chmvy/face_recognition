from django.shortcuts import render
from django.http import HttpResponse
from interface.models import PersonInfo
import json

# Create your views here.

def homepage(request):
    return render(request, 'interfacematerial/index.html')

def heartback(request):
    return HttpResponse(str({
        "resultCode": 200,
        "deviceCode": "123134",
        "msg": "成功",
        "SyncState": 1
    }))

def sysetup(request):
    return HttpResponse("设置")

def synperson(request):

    return HttpResponse('人员进出')

def synrecord(request):
    print(request.POST)

def errback(request):
    print(request.POST)


