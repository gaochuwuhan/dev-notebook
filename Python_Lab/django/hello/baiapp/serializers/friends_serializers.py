from rest_framework import serializers
from ..models.friends import Friend

class FriendSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        '''如果想让model对象只序列化某几个字段，fields要是一个元组；
            如果序列化所有字段，直接让fields = '__all__'
        '''
        # fields = (
        #     "f_name",
        #     "addr"
        # )
        fields = '__all__'
        model = Friend