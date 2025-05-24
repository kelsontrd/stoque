import os
import django
from decouple import config

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "seuprojeto.settings"
)  # altere "seuprojeto"
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username=config("DJANGO_SU_USERNAME")).exists():
    User.objects.create_superuser(
        username=config("DJANGO_SUPERUSER_USERNAME"),
        email=config("DJANGO_SUPERUSER_EMAIL"),
        password=config("DJANGO_SUPERUSER_PASSWORD"),
    )
    print("Superusuário criado.")
else:
    print("Superusuário já existe.")
