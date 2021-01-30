from django.shortcuts import render

def baiappindex(request):
    return render(request,'baiapp/index.html') #render渲染的是templates中的baiapp/index.html