from django.http import HttpResponse
from django.shortcuts import render

'''
view的参数一定是request，但返回响应对象可以是三种形式，

-   1. HttpResponse(): 参数是参数为字符串，字符串中写文本内容。如果参数为字符串里含有 html 标签，也可以渲染'''

def httpresponse(request):
    return HttpResponse("返回了httpresponse响应对象")
'''
2. render()渲染 : 
最多三个参数：request, 页面名称（str），字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）

'''
def render(request):
    return render(request,'baiapp/index.html') #name可传给templates
