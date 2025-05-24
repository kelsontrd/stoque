from django.db import models
from django.core.validators import MinValueValidator
from controlstock.models.Unity import Unity


class Product(models.Model):
    cod = models.CharField(max_length=15, unique=True, verbose_name="Código")
    name = models.CharField(max_length=100, verbose_name="Nome")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    unity = models.ForeignKey(
        Unity,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Unidade",
        related_name="produtos",
    )

    sell_without_stock = models.BooleanField(
        default=False, verbose_name="Vender sem estoque"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.name

    def increment_stock(self, quantity):
        self.quantity += quantity
        self.save()

    def decrement_stock(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            self.save()

    def adjust_stock(self, quantity, operation):
        if operation:
            self.increment_stock(quantity)
        else:
            self.decrement_stock(quantity)
            
    class Meta:
        ordering = ['id']
