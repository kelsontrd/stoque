from django.db import models

class Unity(models.Model):
    name = models.CharField(max_length=20, verbose_name="Unidade")
    abbreviation = models.CharField(max_length=4, verbose_name="Abreviação")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    def __str__(self):
        return self.abbreviation
    