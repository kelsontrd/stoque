from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from controlstock.models.OperationDescription import OperationDescription
from controlstock.models.Product import Product


class EntryProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True,
        verbose_name="Produto", related_name="entradas"
    )
    operation_description = models.ForeignKey(
        OperationDescription, on_delete=models.SET_NULL, null=True,
        verbose_name="Tipo de operação", related_name="entradas"
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], verbose_name="Quantidade"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        product_name = self.product.name if self.product else "Produto removido"
        return f"{product_name} - ({self.quantity})"

    def clean(self):
        super().clean()

        if self.operation_description:
            if not self.operation_description.type_operation:
                raise ValidationError("Somente operações de Entrada são permitidas neste modelo.")

    def adjust_stock(self):
        if self.product and self.operation_description:
            tipo = self.operation_description.type_operation
            self.product.adjust_stock(self.quantity, tipo)
    
    class Meta:
        ordering = ['id']
