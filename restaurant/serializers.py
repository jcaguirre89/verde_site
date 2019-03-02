from rest_framework import serializers
from restaurant.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MenuItem
        fields = ('id', 'created', 'modified', 'name', 'description', 'category', 'price', 'user')
