from rest_framework.views import APIView
from rest_framework import viewsets
from ..models.friends import Friend
from ..serializers.friends_serializers import FriendSerializers

'''使用viewsets实现对数据的增删改查'''
class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all() #序列化哪些模型
    serializer_class = FriendSerializers    #从序列化文件中选择序列化哪个类




