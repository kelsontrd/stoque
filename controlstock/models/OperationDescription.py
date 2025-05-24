from django.db import models


class OperationDescription(models.Model):
    TIPO_CHOICE = ((True, "Entrada"), (False, "Saída"))
    name = models.CharField(max_length=100, verbose_name="Nome")
    type_operation = models.BooleanField(
        choices=TIPO_CHOICE, default=True, verbose_name="Tipo de operação"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        # Retorna uma string com o nome e o tipo de operação (Entrada ou Saída)
        # return f"{self.name} ({'Entrada' if self.type_operation else 'Saida'})"
        return f"{self.name}"
    
    class Meta:
        ordering = ['id']
