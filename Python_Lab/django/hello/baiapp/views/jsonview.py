from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import logging

logger=logging.getLogger("django")


def user(request):
	# user_list=['bai','hei']
    logger.info("display userlist")
    return JsonResponse([{"bai":"xiaobai","hei":"dahei"}],safe=False)  #这里要将safe设为false才会成功返回