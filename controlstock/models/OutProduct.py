from datetime import datetime, timedelta
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from controlstock.models.OperationDescription import OperationDescription
from django.utils import timezone
from controlstock.models.Product import Product
from controlstock.models.Customer import Customer

class OutProduct(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True,
        verbose_name="Cliente", related_name="saidas"
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True,
        verbose_name="Produto", related_name="saidas"
    )
    operation_description = models.ForeignKey(
        OperationDescription, on_delete=models.SET_NULL, null=True,
        verbose_name="Tipo de operação", related_name="saidas"
    
    )
    
    operation_date = models.DateTimeField(null=True, blank=True,
        verbose_name="Data da operação"
    )
     
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], verbose_name="Quantidade"
    )
   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def save(self, *args, **kwargs):
        if not self.operation_date:
            self.operation_date = self.created_at or timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        product_name = self.product.name if self.product else "Produto removido"
        customer_name = self.customer.name if self.customer else "Cliente removido"
        return f"{product_name} - {customer_name} ({self.quantity})"

    def clean(self):
        super().clean()

        # Garante que a operação seja de saída
        if self.operation_description and self.operation_description.type_operation:
            raise ValidationError("Somente operações de saída são permitidas neste modelo.")

        # Validação de estoque
        if self.product and not self.product.sell_without_stock:
            if self.quantity > self.product.quantity:
                raise ValidationError("Quantidade solicitada excede o estoque disponível.")

        # Restrição de data retroativa
        if self.operation_date:
            hoje = timezone.now()
            limite_data = hoje - timedelta(days=7)
            if self.operation_date < limite_data:
                raise ValidationError("Data retroativa inválida. Máximo permitido: 7 dias atrás.")

            
    def adjust_stock(self):
        if self.product and self.operation_description:
            tipo = self.operation_description.type_operation
            self.product.adjust_stock(self.quantity, tipo)
