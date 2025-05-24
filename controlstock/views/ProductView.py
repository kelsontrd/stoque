from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from controlstock.models.Product import Product
from controlstock.templates.product.ProductForm import ProductForm

# views.py

class ProductListView(ListView):
    model = Product
    template_name = 'product/list_product.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('product_list')
