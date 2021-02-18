'''在子app中添加url'''
from django.urls import path
from django.conf.urls import url,include
from baiapp.views import text,jsonview,render,friends,rest_friends
from rest_framework.routers import DefaultRouter

'''用drf注册路由'''
router=DefaultRouter()
router.register(r'friends',rest_friends.FriendViewset) 
#搭配根url和此文件的url配置，路径为baiapp/drf/friends


urlpatterns = [

    path('1',text.baifirst,name='baifirst1'),
    path('2',text.baisecond),
    path('user',jsonview.user),
    path('render',render.baiappindex) #返回render中的index
]
#django自身的url
urlpatterns += [
    url(r'^friends/$',friends.Friendview.as_view()), #路径为baiapp/firends
    url(r'^friends/(?P<pk>\d+)/$',friends.Friendinfo.as_view())
]

#drf的url
urlpatterns += [
    path('drf/',include(router.urls))
]