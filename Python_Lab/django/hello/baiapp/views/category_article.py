from baiapp.serializers import ArticleSerilizers,CategorySerilizers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from baiapp.models import Article,Category
import logging

from rest_framework.response import Response
from rest_framework import status  #为了返回状态码
from rest_framework.decorators import api_view,APIView  #为了使用视图装饰器

from baiapp.core.django_http import Httpres

logger=logging.getLogger("django")

'''用的是django的http request和response '''

def django_category(request):
    #返回所有书籍
    if request.method == 'GET':
        categorys = Category.objects.all()
        ser = CategorySerilizers(categorys,many=True,context={'request':request})
        # return JsonResponse(ser.data,safe=False)    #返回的是序列化后的json，
        #也可以用httpresponse
        json_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    elif request.method == 'POST': #反序列化
        data = JSONParser().parse(request)  #取出request里的data，转换为python dict
        re_ser = CategorySerilizers(data=data,context={'request':request})
        logger.info("GET data:",type(data),'Get re_ser:',type(re_ser))
        if re_ser.is_valid():
            re_ser.save()
            json_data=JSONRenderer().render(re_ser.data)
            logger.info("GET response data:",type(re_ser.data))  #想看一下返回给用户的数据是什么类型
            # return JsonResponse(re_ser.data,status=201)
            return HttpResponse(json_data,content_type='application/json',status=201)
            
        return JsonResponse(re_ser.errors,status=400)

#获取单个书籍
def category_detail(request,pk):
    '''先对请求的书籍id是否存在做一个判断，不存在则返回404'''
    try:
        cat=Category.objects.get(pk=pk)
    except Category.DoesNotExist as e:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # art=Article.objects.get(pk=pk)
        ser=CategorySerilizers(instance=cat,context={'request':request})
        json_data=ser.data
        return JsonResponse(json_data,status=200)
    elif request.method == 'PUT':
        data=JSONParser().parse(request) #put传body时要把需要的字段都传进来
        ser=CategorySerilizers(instance=cat,data=data,context={'request':request})  #put方法要先把原来的数据调出来，再进行某个字段的更改，所以这个序列化两个参数都要写
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)    #put/post/patch的返回码都是201
        return JsonResponse(ser.errors,status=400)  #没通过校验的返回
    elif request.method == 'PATCH': #patch传body时可以不把所有字段都写进body里，把想改的部分写成json即可
        data=JSONParser().parse(request)
        ser=CategorySerilizers(instance=cat,data=data,partial=True,context={'request':request})  #partial=True代表部分更新，也是对的某个对象进行单/多个/所有字段值的更改
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        return JsonResponse(ser.errors,status=400)
    elif request.method == 'DELETE':
        cat.delete()
        return HttpResponse(status=204)




# '''用的是drf的request/response/status,使用的时候搭配api视图，FBV就是@api_view装饰器，CBV就是 APIView类'''

#基于@api_view示例
# @api_view(["GET","POST"])
# def drf_articleview(request): #参数request用了drf的装饰器以后就不是django里的request了，是drf的
#     if request.method == 'Get':
#         articles=Article.objects.all()
#         ser = ArticleSerilizers(instance=articles, many=True, context={'request': request})
#         return Response(ser.data,status=status.HTTP_200_OK)  #替代django的Httpresponse，将序列化好的数据传到Response即可
#     elif request.method == 'POST':
#         ser = ArticleSerilizers(data=request.data,context={'request': request})
#         if ser.is_valid:
#             ser.save()
#             return Response(ser.data,status=status.HTTP_201_CREATED)
#         return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST) #没序列化成功的返回error

    
# #基于类视图@      