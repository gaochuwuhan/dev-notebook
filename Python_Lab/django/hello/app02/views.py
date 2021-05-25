from django.shortcuts import render
from rest_framework import generics
from .serializers import GameSerializer
from .models import Game
from rest_framework.authentication import SessionAuthentication,BaseAuthentication

# Create your views here.

class Gamelist(generics.ListCreateAPIView):
    queryset=Game.objects.all()
    serializer_class=GameSerializer

    def perform_create(self,serializer): #想实现新建一个游戏看是哪个用户建的，那么就要看ListCreateAPIView的create方法
        serializer.save(user=self.request.user)  #取出当前用户，要看谁给request.user赋的值，去看BaseAuthentication

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Game.objects.all()
    serializer_class=GameSerializer