# views.py
from django.views.generic import ListView
from controlstock.models.Product import Product

class ProductReportView(ListView):
    model = Product
    template_name = 'product/report/product_report.html'
    context_object_name = 'products'
