from baiapp.serializers import ArticleSerilizers
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from baiapp.models import Article
import logging

logger=logging.getLogger("django")

def article_list(request):
    
    if request.method == 'GET':
        articles = Article.objects.all()
        ser = ArticleSerilizers(articles,many=True)
        return JsonResponse(ser.data,safe=False)    #返回的是序列化后的json
    
    elif request.method == 'POST': #反序列化
        data = JSONParser().parse(request)  #是一个python dict
        re_ser = ArticleSerilizers(data=data)
        logger.info("GET data:",type(data),'Get re_ser:',type(re_ser))
        if re_ser.is_valid():
            re_ser.save()
            logger.info("GET response data:",type(re_ser.data))  #想看一下返回给用户的数据是什么类型
            return JsonResponse(re_ser.data,status=201)
            
        return JsonResponse(re_ser.errors,status=400)
