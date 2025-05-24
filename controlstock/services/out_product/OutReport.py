from django.utils import timezone
from controlstock.models.OutProduct import OutProduct
from controlstock.models.Product import Product
from controlstock.models.Customer import Customer

class OutReport:
    @staticmethod
    def geral(data_inicio=None, data_fim=None):
        queryset = OutProduct.objects.all()
        if data_inicio:
            queryset = queryset.filter(operation_date__date__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(operation_date__date__lte=data_fim)
        return queryset

    @staticmethod
    def por_cliente(cliente_id, data_inicio=None, data_fim=None):
        queryset = OutProduct.objects.filter(customer_id=cliente_id)
        if data_inicio:
            queryset = queryset.filter(operation_date__date__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(operation_date__date__lte=data_fim)
        return queryset

    @staticmethod
    def por_produto(produto_id, data_inicio=None, data_fim=None):
        queryset = OutProduct.objects.filter(product_id=produto_id)
        if data_inicio:
            queryset = queryset.filter(operation_date__date__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(operation_date__date__lte=data_fim)
        return queryset
