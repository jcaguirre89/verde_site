import datetime

from django.db import models


# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    pub_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        if self.pub_date is not None and self.pub_date <= datetime.datetime.today().date():
            return True
        return False