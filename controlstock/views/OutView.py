from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from controlstock.models.OutProduct import OutProduct
from controlstock.templates.out_product.OutProductForm import OutProductForm

# views.py

class OutProductListView(ListView):
    model = OutProduct
    template_name = 'out_product/out_product_list.html'
    context_object_name = 'out_products'

class OutProductCreateView(CreateView):
    model = OutProduct
    form_class = OutProductForm
    template_name = 'out_product/out_product_form.html'
    success_url = reverse_lazy('out_product_list')

class OutProductUpdateView(UpdateView):
    model = OutProduct
    form_class = OutProductForm
    template_name = 'out_product/out_product_form.html'
    success_url = reverse_lazy('out_product_list')

class OutProductDeleteView(DeleteView):
    model = OutProduct
    template_name = 'out_product/out_product_delete.html'
    success_url = reverse_lazy('out_product_list')
