# create_superuser.py
from decouple import config
from django.contrib.auth import get_user_model

def run():
    User = get_user_model()
    username = config("DJANGO_SUPERUSER_USERNAME")
    email = config("DJANGO_SUPERUSER_EMAIL")
    password = config("DJANGO_SUPERUSER_PASSWORD")

    if not User.objects.filter(username=username).exists():
        print("Criando superusuário...")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superusuário criado com sucesso!")
    else:
        print("Superusuário já existe.")
