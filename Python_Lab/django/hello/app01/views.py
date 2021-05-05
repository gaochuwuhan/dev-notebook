from django.shortcuts import render

# Create your views here.
from hello.core.django_http import Httpres
from app01.models import User as app01user
from app01.serializers import UserSerializers
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

def users(request):
    httpres=Httpres(md=app01user,pk=None,slz=UserSerializers)
    if request.method == 'GET':
        return httpres.getall(request=request)
    elif request.method == "POST":
        return httpres.postmd(request=request)

def user_detail(request,pk):
    httpres=Httpres(md=app01user,pk=pk,slz=UserSerializers)
    try:
        u=httpres.md.objects.get(pk=pk)
    except httpres.md.DoesNotExist as e:
        return HttpResponse(status=404)
    if request.method == 'GET':
        return httpres.getmd()
    if request.method == 'PUT':
        return httpres.putmd(request=request,instance=u)
    if request.method == 'PATCH':
        return httpres.patchmd(request=request,instance=u)
    if request.method == 'DELETE':
        return httpres.deletemd(instance=u)    

'''用drf的apiview装饰器'''
@api_view(['GET','POST'])
def user_list(request): #这个request参数就是drf的request
    if request.method == 'GET':
        user=app01user.objects.all()
        ser=UserSerializers(instance=user,many=True,context={'request':request})
        return Response(ser.data,status.HTTP_200_OK)
    elif request.method == 'POST':
        ser=UserSerializers(data=request.data,context={'request':request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status.HTTP_201_CREATED)
        return Response(ser.errors,status.HTTP_400_BAD_REQUEST)

'''用drf的类视图'''
class User_detail(APIView):

    def get_object(self,pk):
        try:
            u = app01user.objects.get(pk=pk)
            return u
        except Exception as e:
            raise Http404() 

    def get(self,request,*args,**kwargs):
        u = self.get_object(kwargs.get('pk'))
        ser = UserSerializers(instance=u,context={'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        u = self.get_object(kwargs.get('pk'))
        ser = UserSerializers(instance=u,data=request.data, context={'request':request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        u = self.get_object(kwargs.get('pk'))
        ser = UserSerializers(instance=u,data=request.data, context={'request':request},partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        u = self.get_object(kwargs.get('pk'))
        u.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
