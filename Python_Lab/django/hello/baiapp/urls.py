'''在子app中添加url'''
from django.urls import path
from baiapp.views import text,jsonview,render
urlpatterns = [
    # path('',views.baifirst,name='baifirst'),
    path('1',text.baifirst,name='baifirst1'),
    path('2',text.baisecond),
    path('user',jsonview.user),
    path('render',render.baiappindex) #返回render中的index
]