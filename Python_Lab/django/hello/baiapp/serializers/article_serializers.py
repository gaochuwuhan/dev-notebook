from rest_framework import serializers
from baiapp.models.article import Article

class ArticleSerilizers(serializers.Serializer): #普通序列化
    '''serializers.Serializer相对于serializers.ModelSerializer要把所有字段的限制也写上'''
    id = serializers.IntegerField(read_only=True)  #由于数据库表id是一个自动生成的字段，所以设定read_only=True不允许更改
    title = serializers.CharField(required=True,max_length=100) #required=True代表必要字段
    vnum = serializers.IntegerField(required=True)
    content = serializers.CharField()

    '''一般重写Serializer的create方法，create和update方法都要校验后入库。inctance代表更新的实例'''

    def create(self,validated_data): #validated_data就是一个json,是传过来的字段信息
        return Article.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.tiele = validated_data.get('title',instance.tiele) #validated_data.get把对应更新的实例的字段取出
        instance.vnum = validated_data.get('vnuAm',instance.vnum)
        instance.content = validated_data.get('content',instance.content)

        instance.save()
        return instance
        


    # 参数约束:
    # read only:True表示不允许用户自己上传，只能用于api的输出
    # write only:
    # required:字段是否必填
    # allow_null/allow_blank:是够允许为null/空 


    