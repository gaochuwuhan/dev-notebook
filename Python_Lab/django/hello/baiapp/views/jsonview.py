from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json


def user(request):
	# user_list=['bai','hei']
    return JsonResponse([{"bai":"xiaobai","hei":"dahei"}],safe=False)  #这里要将safe设为false才会成功返回