from django.db import models

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='articles')