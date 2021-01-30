"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''在根url（主路由）中添加app中的子url
Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name

route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。

view: 用于执行与正则表达式匹配的 URL 请求。

kwargs: 视图使用的字典类型的参数。

name: 用来反向获取 URL。
'''
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views
from baiapp import urls
from .views import render

urlpatterns = [ #django默认的admin页面
    url('admin/', admin.site.urls), #路径就是route；admin.site.urls就是view参数
]
urlpatterns += [    #意思是urlpatterns=urlpatterns+后面的path
    path ('baiapp/', include('baiapp.urls')),  #去子app中将url路径写到include中，则访问“127.0.0.1:8000/baifirst/baiapp.urls的path/” 就能访问到bai.view 的response
]

