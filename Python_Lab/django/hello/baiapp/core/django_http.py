from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

'''做一个django的http封装，每个http方法返回响应只需调取此类相应的方法即可'''
class Httpres:
    def __init__(self,md,pk,slz): #md是查询的model，pk是单个查询时得到pk值，slz是用到的序列化类
        self.md=md
        self.pk=pk
        self.slz=slz

    def getall(self,request):    #对整张表查询
        qs=self.md.objects.all()
        ser=self.slz(instance=qs,many=True,context={'request':request})
        json_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_data,content_type='application/json',status=200)


    def getmd(self):    #对单个对象进行查询
        qs=self.md.objects.get(pk=self.pk) #qs是queryset
        ser=self.slz(instance=qs)   #序列化
        json_data=JSONRenderer().render(ser.data) #渲染成json
        return HttpResponse(json_data,content_type='application/json',status=200)
    
    def postmd(self,request):   #新增单个对象
        dict_data=JSONParser().parse(request)
        ser=self.slz(data=dict_data)
        if ser.is_valid():
            ser.save()
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json',status=201)
        return JsonResponse(ser.errors,status=400)

    def putmd(self,request,instance):   #更新单个对象，需要输入所有字段
        dict_data=JSONParser().parse(request)
        ser=self.slz(instance=instance,data=dict_data)
        if ser.is_valid():
            ser.save()
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json',status=201)
        return JsonResponse(ser.errors,status=400)
    
    def patchmd(self,request,instance): #更新单个对象部分字段，只需输入更新的字段即可
        dict_data=JSONParser().parse(request)
        ser=self.slz(instance=instance,data=dict_data,partial=True)
        if ser.is_valid():
            ser.save()
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json',status=201)
        return JsonResponse(ser.errors,status=400)
    
    def deletemd(self,instance):    #删除单个对象
        instance.delete()
        return HttpResponse(status=204)