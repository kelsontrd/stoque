from django.db import models
from controlstock.validators.phone_number_validator import phone_number_validator

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    phone_number = models.CharField(max_length=17, validators=[phone_number_validator], null=True, verbose_name="Telefone")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    def __str__(self):
        return self.name
    