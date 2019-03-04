from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    price = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=False, help_text=_('Check box if this item currently in the menu'))
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.name

