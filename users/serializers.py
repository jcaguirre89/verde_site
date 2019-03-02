from rest_framework import serializers


from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    menu_items = serializers.HyperlinkedRelatedField(many=True, view_name='menuitem-detail', read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name',
                  'last_name', 'date_joined', 'menu_items', 'articles')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """ Overwrite create method to use the User create_user method instead of just create """
        user = User.objects.create_user(**validated_data)
        return user