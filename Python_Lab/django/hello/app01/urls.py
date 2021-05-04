'''在子app中添加url'''
from django.urls import path
from django.conf.urls import url,include
from app01.views import users
from rest_framework.routers import DefaultRouter

'''用drf注册路由'''
router=DefaultRouter()

urlpatterns = [
]


#drf的url
urlpatterns += [
    path('drf/',include(router.urls)),
    path('drf/app01_users/',users,name='app01_users'),
]
