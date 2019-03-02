from django.db import models

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='articles')