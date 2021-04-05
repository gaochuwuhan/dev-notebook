from baiapp.serializers import ArticleSerilizers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from baiapp.models import Article
import logging

from rest_framework.response import Response
from rest_framework import status  #为了返回状态码
from rest_framework.decorators import api_view,APIView  #为了使用视图装饰器

logger=logging.getLogger("django")

'''用的是django的http request和response '''

def django_article(request):
    
    if request.method == 'GET':
        articles = Article.objects.all()
        ser = ArticleSerilizers(articles,many=True)
        # return JsonResponse(ser.data,safe=False)    #返回的是序列化后的json，
        #也可以用httpresponse
        json_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    elif request.method == 'POST': #反序列化
        data = JSONParser().parse(request)  #取出request里的data，转换为python dict
        re_ser = ArticleSerilizers(data=data)
        logger.info("GET data:",type(data),'Get re_ser:',type(re_ser))
        if re_ser.is_valid():
            re_ser.save()
            json_data=JSONRenderer().render(re_ser.data)
            logger.info("GET response data:",type(re_ser.data))  #想看一下返回给用户的数据是什么类型
            # return JsonResponse(re_ser.data,status=201)
            return HttpResponse(json_data,content_type='application/json',status=201)
            
        return JsonResponse(re_ser.errors,status=400)

'''用的是drf的request/response/status,使用的时候搭配api视图，FBV就是@api_view装饰器，CBV就是 APIView类'''

#基于@api_view示例
@api_view(["GET","POST"])
def drf_articleview(request): #参数request用了drf的装饰器以后就不是django里的request了，是drf的
    if request.method == 'Get':
        articles=Article.objects.all()
        ser = ArticleSerilizers(instance=articles, many=True, context={'request': request})
        return Response(ser.data,status=status.HTTP_200_OK)  #替代django的Httpresponse，将序列化好的数据传到Response即可
    elif request.method == 'POST':
        ser = ArticleSerilizers(data=request.data,context={'request': request})
        if ser.is_valid:
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST) #没序列化成功的返回error

    
#基于类视图@      