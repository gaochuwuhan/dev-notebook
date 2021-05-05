'''在子app中添加url'''
from django.urls import path
from django.conf.urls import url,include
from app01.views import users,user_detail,user_list,User_detail
from rest_framework.routers import DefaultRouter

'''用drf注册路由'''
router=DefaultRouter()

urlpatterns = [
]


#drf的url
urlpatterns += [
    path('drf/',include(router.urls)),
    path('drf/app01_users/',users,name='app01_users'),
    path('drf/app01_users/<int:pk>/',user_detail,name='user_detail'),
    path('drf/app01_userfbv/',user_list,name='user_fbv'), #drf视图的fbv
    path('drf/app01_usercbv/<int:pk>/',User_detail.as_view(),name='user_cbv'),#drf 视图的cbv
]
