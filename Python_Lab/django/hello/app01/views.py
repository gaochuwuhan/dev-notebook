from django.shortcuts import render

# Create your views here.
from hello.core.django_http import Httpres
from app01.models import User as app01user
from app01.serializers import UserSerializers

def users(request):
    httpres=Httpres(md=app01user,pk=None,slz=UserSerializers)
    if request.method == 'GET':
        return httpres.getall(request=request)
    elif request.method == "POST":
        return httpres.postmd(request=request)
        