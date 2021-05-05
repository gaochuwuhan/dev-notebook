from rest_framework import serializers
from app01.models import User as app01user
import re
from hello.core.logger import logger

class UserSerializers(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11,min_length=11,required=True) #重写phone的字段
    pwd1 = serializers.CharField(write_only=True) #由于ModelSerializer默认只序列化model里有的字段，所以我这里添加一个没有的字段，属性是write_only
    class Meta:
        model = app01user
        fields = '__all__'

        extra_kwargs = {
            "pwd": {"write_only":True}
        }
    
    def to_representation(self,instance):
        representation = super(UserSerializers,self).to_representation(instance)
        representation['gender'] = instance.get_gender_display() #返回当前实例的gender字段的display
        return representation
        
    #当我们序列化的时候会执行这个验证函数
    def validate_phone(self,phone):  #单独的验证函数。格式就是validate_xx，xx一定是model中或者序列化中的一个字段
        if not re.match(r'1[3456789]\d{9}',phone): #正则判断手机号是否符合
            logger.info(f'传过来的手机号是:',phone)
            raise serializers.ValidationError('手机号不合法') #不符合则抛出验证异常
        
        if app01user.objects.filter(phone=phone).all():
            logger.info('从数据表中查询传来的手机号',app01user.objects.filter(phone=phone).all())
            raise serializers.ValidationError('手机号已被注册')
        return phone #一定要返回验证的值，正确的话一定要返回给用户
    
    
    def validate(self,attrs): #最终组合验证函数，attrs代表所有的字段
        if attrs.get('pwd1') != attrs.get('pwd'):
            raise serializers.ValidationError('密码不一致')
        if 'pwd1' in attrs: #如果是patch方法的话有可能不传pwd1的值，所以要做一个判断是否存在pwd1
            attrs.pop('pwd1') #如果两次密码一致的话，要从attrs里拿掉pwd1因为不存到数据库
        return attrs