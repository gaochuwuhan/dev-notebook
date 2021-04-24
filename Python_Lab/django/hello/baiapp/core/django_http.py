from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

'''做一个django的http封装，每个http方法返回响应只需调取此类相应的方法即可'''
class Httpres:
    def __init__(self,md,pk,slz):
        self.md=md
        self.pk=pk
        self.slz=slz

    def getmd(self):
        qs=self.md.objects.get(pk=self.pk)
        ser=self.slz(instance=qs)
        json_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    def postmd(self,request):
        dict_data=JSONParser().parse(request)
        ser=self.slz(data=dict_data)
        if ser.is_valid():
            ser.save()
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json',status=201)
        return JsonResponse(ser.errors,status=400)

    def putmd(self,request,instance):
        dict_data=JSONParser().parse(request)
        ser=self.slz(instance=instance,data=dict_data)
        if ser.is_valid():
            ser.save()
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json',status=201)
        return JsonResponse(ser.errors,status=400)
    
    def patchmd(self,request,instance):
        dict_data=JSONParser().parse(request)
        ser=self.slz(instance=instance,data=dict_data,partial=True)
        if ser.is_valid():
            ser.save()
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json',status=201)
        return JsonResponse(ser.errors,status=400)