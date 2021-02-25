from rest_framework import viewsets
from serializers.article_serializers import ArticleSerilizers
from models.article import Article

class ArticleViewsets(viewsets.ModelViewSet):
    serializer_class = ArticleSerilizers
    queryset =  Article.objects.all()

