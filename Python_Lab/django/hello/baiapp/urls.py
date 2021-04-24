'''在子app中添加url'''
from django.urls import path
from django.conf.urls import url,include
from baiapp.views import ArticleViewsets
from baiapp.views import (
    text,jsonview,render,friends,rest_friends,normal_article,category_article,one2one
)
from rest_framework.routers import DefaultRouter

'''用drf注册路由'''
router=DefaultRouter()
router.register(r'friends',rest_friends.FriendViewset) 
#搭配根url和此文件的url配置，路径为baiapp/drf/friends

router.register(r'article',ArticleViewsets)
# router.register(r'normalarticle',normal_article.article_list)

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
    path('drf/',include(router.urls)),
    path('drf/django_article/',normal_article.django_article),
    path('drf/django_category/',category_article.django_category,name='category_list'),
    path('drf/category_detail/<int:pk>/',category_article.category_detail,name='category_detail'),
    path('drf/drf_article/',normal_article.drf_articleview,name='article_list'),
    path('drf/django_article/<int:pk>/',normal_article.article_detail,name='article_detail'), #int里的pk是因为view中的函数pk
    path('drf/account_detail/<int:pk>/',one2one.account_detail,name='account_detail'), #测试onetoone主表
    path('drf/contact_detail/<int:pk>/',one2one.contact_detail,name='contact_detail'), #测试onetoone关联表单条
    path('drf/card_contact/',one2one.card_contact,name='card_contact'),#测试onetoone关联表所有数据

]