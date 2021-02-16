from django import http
from ..models.friends import Friend
from django.views import View
import json
from django.http import HttpResponse

'''baiapp/friends/列表视图'''
class Friendview(View):
    #获取所有朋友
    def get(self,request):
        '''1.获取所有friends'''
        friends = Friend.objects.all()
        '''2.数据转换'''
        friends_list = []
        for f in friends:
            f_dict = {
                "id":f.id,
                "f_name":f.f_name,
                "address":f.addr,
                "classroom":f.grade_id,
            }
            friends_list.append(f_dict)
        '''3.返回响应'''
        #将列表能序列化成json要将jsonresponse的safe选项设定为false
        return http.JsonResponse(friends_list,safe=False) 

    #增加models对象
    def post(self,request):
        '''1.获取参数'''
        #后端，通过request.body接收数据，request.body是byte类型，直接使用json.loads解析，先decode一下
        #如果使用simplejson.loads(request.body)，就不用decode()
        dict_data=json.loads(request.body.decode()) #用户传过来的body是一个json字符串,json.loads()将其转化成字典
        f_name=dict_data.get("f_name") #提取字典的value
        addr=dict_data.get("addr")
        grade_id=dict_data.get("grade_id")
        '''2.校验参数'''
        #先略
        '''3.数据入库'''
        newfriend=Friend.objects.create(**dict_data)  #字典转成model对象
        '''4.返回响应'''
        #为了返回response，将得到的对象拿出对应的值
        friend_dict={
            "id":newfriend.id,
            "f_name":newfriend.f_name,
            "addr":newfriend.addr,
            "grade_id":newfriend.grade_id,
        }
        return http.JsonResponse(friend_dict,status=201)

'''baiapp/friends/pk列表视图'''

class Friendinfo(View):
    '''1.通过pk值获取单个参数'''
    def get(self,request,pk):
        friend=Friend.objects.get(pk=pk)
        friendfict={
            "id":friend.id,
            "f_name":friend.f_name,
            "addr":friend.addr,
            "grade_id":friend.grade_id,
        }
        return http.JsonResponse(friendfict)

    ''' 修改单个对象'''
    def put(self,request,pk):
        '''1.获取参数'''
        dict_data = json.loads(request.body.decode())
        '''2.校验参数'''
        '''3.数据入库'''
        update = Friend.objects.filter(pk=pk).update(**dict_data) #返回的是一个整数，更新了几行，不是对象
        #相当于传一个字典参数，更新多个字段,参考Python_Lab/OO/fun/para.py

        '''4.返回响应'''
        new=Friend.objects.get(pk=pk)
        ret = {
            "id":new.id,
            "f_name":new.f_name,
            "addr":new.addr,
            "grade_id":new.grade_id,
        }
        return http.JsonResponse(ret)

    '''删除单个对象'''
    def delete(self,request,pk):
        '''1.查询对象'''
        Friend.objects.filter(pk=pk).delete()
        #下面是我写的校验数据库是否存在刚才删除的对象，但可以用http状态吗204去代表删除成功
        # verify=Friend.objects.filter(pk=pk)
        # if len(verify) == 0:
        #     return http.JsonResponse({'result':'success deleted'},safe=False)
        return HttpResponse(status=204)



