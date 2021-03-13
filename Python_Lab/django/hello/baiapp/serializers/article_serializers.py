# from rest_framework import serializers
# from models.article import Article

# class ArticleSerilizers(serializers.Serializer): #普通序列化
#     '''serializers.Serializer相对于serializers.ModelSerializer要把所有字段的限制也写上'''
#     id = serializers.IntegerField(read_only=True)  #由于数据库表id是一个自动生成的字段，所以设定read_only=True不允许更改
#     title = serializers.CharField(required=True,max_length=100) #required=True代表必要字段
#     vum = serializers.CharField(max_length=1000)

#     def create(self,validated_data): #validated_data就是一个json
#         return Article.objects.create(**validated_data)
    
#     # def update(self,instance,validated_data):




    