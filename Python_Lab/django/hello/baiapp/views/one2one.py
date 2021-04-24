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

def card_account(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        ser = AccountSerializers(accounts,many=True,context={'request':request})
        # return JsonResponse(ser.data,safe=False)    #返回的是序列化后的json，
        #也可以用httpresponse
        json_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    elif request.method == 'POST': #反序列化
        data = JSONParser().parse(request)  #取出request里的data，转换为python dict
        re_ser = AccountSerializers(data=data,context={'request':request})
        logger.info("GET data:",type(data),'Get re_ser:',type(re_ser))
        if re_ser.is_valid():
            re_ser.save()
            json_data=JSONRenderer().render(re_ser.data)
            logger.info("GET response data:",type(re_ser.data))  #想看一下返回给用户的数据是什么类型
            # return JsonResponse(re_ser.data,status=201)
            return HttpResponse(json_data,content_type='application/json',status=201) #不加content_type=json就会默认返回html
            
        return JsonResponse(re_ser.errors,status=400)

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


    






def card_contact(request):
    if request.method == 'GET':
        con=Contact.objects.all()
        ser=ContactSerializers(instance=con,many=True)
        json_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
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
      