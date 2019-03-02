from django.db import models
from django.utils import timezone


class MenuItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    price = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.name

