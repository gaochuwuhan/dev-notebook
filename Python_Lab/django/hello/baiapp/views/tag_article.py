from baiapp.core.django_http import Httpres
from baiapp.models import Tag
from baiapp.serializers import TagSerializers
from django.http import HttpResponse


def django_tag(request):
    httpres=Httpres(md=Tag,slz=TagSerializers,pk=None) #因为是查询整个表，所以pk=None
    if request.method == 'GET':
        return httpres.getall(request=request) #把request传到context里

    elif request.method == 'POST': #反序列化
        return httpres.postmd(request=request)

def tag_detail(request,pk):
    httpres=Httpres(md=Tag,slz=TagSerializers,pk=pk)
    if request.method == 'POST': #由于post是新增一行，所以不用判定是否存在
        return httpres.postmd(request=request)
    else:    
        try:
            tag=httpres.md.objects.get(pk=pk)
        except httpres.md.DoesNotExist as e:
            return HttpResponse(status=404)
        if request.method == 'GET':
            return httpres.getmd()
        if request.method == 'PUT':
            return httpres.putmd(request=request,instance=tag)
        if request.method == 'PATCH':
            return httpres.patchmd(request=request,instance=tag)
        if request.method == 'DELETE':
            return httpres.deletemd(instance=tagc)    
        
