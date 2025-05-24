# validators.py ou no topo do models.py
from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos."
)
