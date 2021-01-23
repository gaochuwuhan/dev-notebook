'''在子app中添加url'''
from django.urls import path

from . import views

urlpatterns = [
    # path('',views.baifirst,name='baifirst'),
    path('1',views.baifirst,name='baifirst1'),
    path('2',views.baisecond),
]