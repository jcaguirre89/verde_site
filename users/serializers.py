from rest_framework import serializers


from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    menu_items = serializers.HyperlinkedRelatedField(many=True, view_name='menuitem-detail', read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'date_joined', 'menu_items', 'articles')