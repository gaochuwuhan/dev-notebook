from rest_framework import serializers
from baiapp.models.article import Article,Category,Tag

#普通序列化
# class ArticleSerilizers(serializers.Serializer): 
#     '''serializers.Serializer相对于serializers.ModelSerializer要把所有字段的限制也写上'''
#     id = serializers.IntegerField(read_only=True)  #由于数据库表id是一个自动生成的字段，所以设定read_only=True不允许更改
#     title = serializers.CharField(required=True,max_length=100) #required=True代表必要字段
#     vnum = serializers.IntegerField(required=True)
#     content = serializers.CharField()

#     '''一般重写Serializer的create方法，create和update方法都要校验后入库。inctance代表更新的实例'''

#     def create(self,validated_data): #validated_data就是一个json,是传过来的字段信息
#         return Article.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.tiele = validated_data.get('title',instance.tiele) #validated_data.get把对应更新的实例的字段取出
#         instance.vnum = validated_data.get('vnuAm',instance.vnum)
#         instance.content = validated_data.get('content',instance.content)

#         instance.save()
#         return instance
        


    # 参数约束:
    # read only:True表示不允许用户自己上传，只能用于api的输出
    # write only:
    # required:字段是否必填
    # allow_null/allow_blank:是够允许为null/空 


    

'''模型序列化:已经封装好了create和update方法，一般不需要重写，但根据需求可以重写'''
# class ArticleSerilizers(serializers.ModelSerializer):
    
#     # category = serializers.StringRelatedField() #返回一个字符串，文章查分类的时候是多对一
#     # category = serializers.PrimaryKeyRelatedField(read_only=True) #查询article的category字段变成Category的id，read_only=True要填不然报错
#     # category = serializers.HyperlinkedRelatedField(
#     #     view_name='category_detail', #因为点进去跳的是分类的详情，所以拿的是category_detail的view name
#     #     read_only=True,

#     #     )
#     # category = serializers.SlugRelatedField(
#     #     slug_field='name', #想让查询文章的时候category字段返回Category表的name字段
#     #     read_only=True,
#     # )
#     category = serializers.HyperlinkedIdentityField(
#         view_name='category_detail', #必写字段
#         lookup_field='pk',
        
#     )
#     class Meta:
#         model =  Article
#         # fields = ('id','vnum','title','content')  #如果没有序列化/或者不存在的key用户写在了字典里，只要包涵'vnum','title'两个字段就能post成功
#         fields = '__all__'
# class CategorySerilizers(serializers.ModelSerializer):

#     # articles_category = serializers.StringRelatedField(many=True) #由于一个分类对应多个文章，所以要加many=True,articles_category就是article model中外键的related_name
#     # articles_category = serializers.PrimaryKeyRelatedField(read_only=True,many=True) #查询分类的路由返回articles_category的值是article的id
#     # articles_category = serializers.HyperlinkedRelatedField(
#     #     view_name='article_detail',
#     #     many=True,
#     #     read_only=True,
#     # )
#     # articles_category = serializers.SlugRelatedField(

#     #    slug_field='title',
#     #    many=True, 
#     #    read_only=True,

#     # )
#     articles_category = serializers.HyperlinkedIdentityField(
#         view_name='article_detail',
#         many=True,
#     )
#     class Meta:
#         model = Category
#         fields = '__all__'

#HyperlinkedModelSerializer
# class ArticleSerilizers(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model =  Article
#         # fields = ('id','vnum','title','content')  #如果没有序列化/或者不存在的key用户写在了字典里，只要包涵'vnum','title'两个字段就能post成功
#         fields = '__all__'

#         extra_kwargs = {
#             'url':{'view_name':'article_detail','lookup_field':'pk'},
#             'category':{'view_name':'category_detail','lookup_field':'pk'}
#         }

# class CategorySerilizers(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Category
#         fields = ('id','name','articles_category','url')
        
#         extra_kwargs = {
#             'url':{'view_name':'category_detail','lookup_field':'pk'}, #多返回一个自身url的字段
#             'articles_category':{'view_name':'article_detail','lookup_field':'pk'}
#         }


#序列嵌套

# class ArticleSerilizers(serializers.ModelSerializer):

#     class Meta:
#         model =  Article
#         # fields = ('id','vnum','title','content')  #如果没有序列化/或者不存在的key用户写在了字典里，只要包涵'vnum','title'两个字段就能post成功
#         fields = '__all__'


# class CategorySerilizers(serializers.ModelSerializer):

#     articles_category=ArticleSerilizers(many=True)  #将反向查找的序列化的字段设定为所有符合的articles的所有字段
#     class Meta:
#         model = Category
#         fields = ('id','name','articles_category')


#depth
# class ArticleSerilizers(serializers.ModelSerializer):

#     class Meta:
#         model =  Article
#         # fields = ('id','vnum','title','content')  #如果没有序列化/或者不存在的key用户写在了字典里，只要包涵'vnum','title'两个字段就能post成功
#         fields = '__all__'
#         depth = 3

# class CategorySerilizers(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = ('id','name','articles_category')

#serializerMethodField，想返回分类的书籍数量    
# class ArticleSerilizers(serializers.ModelSerializer):

#     class Meta:
#         model =  Article
#         # fields = ('id','vnum','title','content')  #如果没有序列化/或者不存在的key用户写在了字典里，只要包涵'vnum','title'两个字段就能post成功
#         fields = '__all__'
#         depth = 3

# class CategorySerilizers(serializers.ModelSerializer):
#     count = serializers.SerializerMethodField()  #加一个数量的序列化
#     class Meta:
#         model = Category
#         fields = ('id','name','articles_category','count') #记得将count加进来
    
#     def get_count(self,obj):   #这个函数名字是有规律的，get_固定，count是上面定义的名字；参数obj代表当前model的对象
#         # return 10 #随便返回一个10，这样不管是分类几返回的书籍数量都是10
#         return obj.articles_category.count() #统计分类对象的反向查询字段articles_category的数量，引用了orm的count()方法

#source
class MyCharField(serializers.CharField): #定义自己想返回string字段类，为了使想用的正式序列化类继承此类
    #决定每个字段的返回值
    def to_representation(self,value): #重写to_representation方法，为了使继承这个类的序列化类能返回指定的字段
        data_list=[]
        for var in value:
            data_list.append({"title":var.title,"content":var.content}) #想让data_list是一个多个字典的list，字典中包含title和content字段
        return data_list
class ArticleSerilizers(serializers.ModelSerializer):

    # category = serializers.IntegerField(source='category.id') #返回关联表的id字段
    class Meta:
        model = Article
        fields = '__all__'
    
    def to_representation(self,instance): #instance代表当前文章的实例
        representation = super(ArticleSerilizers,self).to_representation(instance)
        representation['category'] = CategorySerilizers(instance.category).data.pop('name')
        representation['tags'] = [t.pop('name') for t in TagSerializers(instance.tags,many=True).data ]
        return representation


class CategorySerilizers(serializers.ModelSerializer):

    # arts = MyCharField(source='articles_category.all')  #arts返回的是符合条件的article的quueryset,source的值会作为参数传到MyCharField的to_representation函数中给value
    class Meta:
        model = Category
        fields = ('id','name','articles_category')

class TagSerializers(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = Tag
        fields = '__all__'