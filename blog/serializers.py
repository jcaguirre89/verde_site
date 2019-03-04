from rest_framework import serializers
from blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Article
        fields = ('id', 'created', 'modified', 'title', 'abstract',
                  'content', 'pub_date', 'is_published', 'user')
