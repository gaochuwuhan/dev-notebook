'''在子app中添加view

每个view中的函数的参数一定是request
return的一定是response
通常是
##FBV: function based view
e.g.
def user(request):
	user_list=['bai','hei']
    return HttpResponse(json.dumps((user_list)))

'''
from django.shortcuts import render
from django.http import HttpResponse  
import json
# Create your views here.
def baifirst(request):  #第一个参数必须是request
    return HttpResponse("bai's first respone")
def baisecond(request):
    return HttpResponse("bai's second response")


'''
还有一种从类中定义多个function的形式
CBV: class based view
e.g.
'''
# from django.views import View
# class StudentsViews(View):
#     def get(self,request,*args,**kwargs):
#         return HttpResponse('Get')
#     def post(self,request,*args,**kwargs):
#         return HttpResponse('Post')
#     def put(self,request,*args,**kwargs):
#         return HttpResponse('Put')
#     def delete(self,request,*args,**kwargs):
#         return HttpResponse('delete')