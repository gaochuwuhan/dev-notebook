from rest_framework import serializers
from baiapp.models.friends import Friend

class FriendSerializers(serializers.ModelSerializer): #模型序列化
    
    class Meta:
        
        '''如果想让model对象只序列化某几个字段，fields要是一个元组；
            如果序列化所有字段，直接让fields = '__all__'
        '''
        model = Friend
        # fields = (
        #     "f_name",
        #     "addr"
        # )  #三者取一
        fields = '__all__'  #三者取一
        # exclude = () #表示不返回字段，三者取一
        # read_only_fields = () #设置只读字段，不接受用户更改


       