from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    """
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Username field is required')

        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. ''Unselect this instead of deleting accounts.'
        ),
    )
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_latest_entry(self, related_name):
        """
        Latest entry in a model that has a FK to User, using the given related_name
        Sample usage: if I want the latest entry tied to this user in the model Friends,
        which has the related_name=friends, use as:
        user.get_latest_entry('friends')

        as an alternative to:
        user.friends.all().latest()
        """
        def latest_entry(user_instance):
            qs = getattr(user_instance, related_name, None).all()
            if qs:
                return qs.latest()
            return

        return latest_entry(self)


class Profile(models.Model):
    """
    User input data
    DEMOGRAPHICS
    """

    age = models.PositiveSmallIntegerField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return _(f'Profile for {self.user.username}')


    def get_full_name(self):
        return _(f"{self.first_name} {self.last_name}")

    def get_short_name(self):
        return self.get_full_name()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
