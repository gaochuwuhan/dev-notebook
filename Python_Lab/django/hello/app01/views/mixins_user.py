from rest_framework import mixins,generics
from app01.models import User as app01user
from app01.serializers import UserSerializers

# '''对user整张表操作，只有get和post。继承mixins'''
# class UserMixList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):

#     queryset = app01user.objects.all() #GenericAPIView中有get_queryset返回了queryset
#     #GenericAPIView中有get_serializer_class是返回的这个serializer_class；get_serializer方法返回的是serializer_class(*args, **kwargs)
#     serializer_class = UserSerializers 

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,*kwargs) #返回父类ListModelMixin的list方法

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs) #返回CreateModelMixin的create方法


# '''对user的单条数据操作'''
# class UserMixDetail(mixins.RetrieveModelMixin, #获取单条数据的
#                     mixins.UpdateModelMixin,    #更新单条的
#                     mixins.DestroyModelMixin,   #删除单条的
#                     generics.GenericAPIView):

#     queryset = app01user.objects.all()
#     serializer_class = UserSerializers

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def patch(self,request,*args,**kwargs):
#         kwargs['partial'] = True
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)    

'''使用通用的类视图generics.ListCreateAPIView代替上面的mixin'''
class UserMixList(generics.ListCreateAPIView): #代替mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView
    queryset = app01user.objects.all()
    serializer_class = UserSerializers

class UserMixDetail(generics.RetrieveUpdateDestroyAPIView):  #同样替代上面mixin子类
    queryset = app01user.objects.all()
    serializer_class = UserSerializers

