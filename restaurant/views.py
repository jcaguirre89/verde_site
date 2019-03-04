from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters

class MenuItemFilter(filters.FilterSet):
    """ Add functionality to filter by min/max price"""
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = MenuItem
        fields = ('user', 'category', 'min_price', 'max_price')

class MenuViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MenuItemFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)