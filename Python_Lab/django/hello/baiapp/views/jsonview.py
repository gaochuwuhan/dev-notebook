from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import logging

logger=logging.getLogger("django")


def user(request):
	# user_list=['bai','hei']
    logger.info("display userlist")
    return JsonResponse([{"bai":"xiaobai","hei":"dahei"}],safe=False)  #看源码可以知道只有字典参数可以被序列化为json字符串，所以这里要将safe设为false才会成功返回json字符串