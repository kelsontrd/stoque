# core/scripts/create_superuser.py

from django.contrib.auth import get_user_model
import os

def run():
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

    if not User.objects.filter(username=username).exists():
        print("Criando superusuário...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("Superusuário já existe.")
