from verde_site.settings.common import *

from decouple import config
import dj_database_url


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL_DEV')
    )
}