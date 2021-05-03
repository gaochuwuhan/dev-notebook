from baiapp.serializers import AccountSerializers,ContactSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from baiapp.models import Account,Contact
import logging

from rest_framework.response import Response
from rest_framework import status  #为了返回状态码
from rest_framework.decorators import api_view,APIView  #为了使用视图装饰器

from baiapp.core.django_http import Httpres #导入Django http相应的封装类

logger=logging.getLogger("django")


'''用的是django的http request和response '''

#account model的http请求
def card_account(request):
    httpres=Httpres(md=Account,slz=AccountSerializers,pk=None) #因为是查询整个表，所以pk=None
    if request.method == 'GET':
        return httpres.getall(request=request) #把request传到context里
    
    elif request.method == 'POST': #反序列化
        return httpres.postmd(request=request)

def account_detail(request,pk):
    httpres=Httpres(md=Account,pk=pk,slz=AccountSerializers)
    if request.method == 'POST': #由于post是新增一行，所以不用判定是否存在
        return httpres.postmd(request=request)
    else:    
        try:
            acc=httpres.md.objects.get(pk=pk)
        except httpres.md.DoesNotExist as e:
            return HttpResponse(status=404)  #不存在的行不能做以下四种请求
        if request.method == 'GET':
            return httpres.getmd()
        if request.method == 'PUT':
            return httpres.putmd(request=request,instance=acc)
        if request.method == 'PATCH':
            return httpres.patchmd(request=request,instance=acc)
        if request.method == 'DELETE':
            return httpres.deletemd(instance=acc)

#contact model的http请求

def card_contact(request):
    httpres=Httpres(md=Contact,slz=ContactSerializers,pk=None) #因为是查询整个表，所以pk=None
    if request.method == 'GET':
        return httpres.getall(request=request) #把request传到context里
    elif request.method == 'POST':
        return httpres.postmd(request=request)
    
def contact_detail(request,pk):

    httpres=Httpres(md=Contact,pk=pk,slz=ContactSerializers)
    if request.method == 'POST':
        return httpres.postmd(request=request)
    else:    
        try:
            con=Contact.objects.get(pk=pk)
        except Contact.DoesNotExist as e:
            return HttpResponse(status=404)
        if request.method == 'GET':
            return httpres.getmd()
        if request.method == 'PUT':
            return httpres.putmd(request=request,inctance=con)
      