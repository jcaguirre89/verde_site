from blog.models import Article
from blog.serializers import ArticleSerializer

from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters


class ArticleFilter(filters.FilterSet):

    class Meta:
        model = Article
        fields = ('user', 'title')

class ArticleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArticleFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)