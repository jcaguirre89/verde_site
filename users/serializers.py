from rest_framework import serializers


from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    menu_items = serializers.HyperlinkedRelatedField(many=True, view_name='menu-list', read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-list', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'menu_items', 'articles')