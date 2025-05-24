"""
WSGI config for setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = get_wsgi_application()

# Executar script para criar superusuário
try:
    from core.scripts.create_superuser import run
    run()
except Exception as e:
    print(f"Erro ao criar superusuário: {e}")