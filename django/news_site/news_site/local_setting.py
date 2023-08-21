"""
My security stuff is in my local setting 
"""
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--5^aqetj=sk^7)4x##)zc^+3j&7=wnrp%c25t-=!)lpguw8nx)'
