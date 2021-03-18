from rest_framework import viewsets
from baiapp.serializers.article_serializers import ArticleSerilizers
from baiapp.models.article import Article

class ArticleViewsets(viewsets.ModelViewSet):
    serializer_class = ArticleSerilizers
    queryset =  Article.objects.all()

