'''在子app中添加view'''
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def baifirst(request):  #第一个参数必须是request
    return HttpResponse("bai's first respone")
def baisecond(request):
    return HttpResponse("bai's second response")

