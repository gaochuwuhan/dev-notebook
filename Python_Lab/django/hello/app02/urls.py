from .views import Gamelist,GameDetail

from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
]
urlpatterns += [
    path('renzheng/gamelist/',Gamelist.as_view(),name='gamelist'), #整张表
    path('renzheng/gamedetail/<int:pk>/',GameDetail.as_view(),name='gamedetail'),#drf mixins的cbv
]