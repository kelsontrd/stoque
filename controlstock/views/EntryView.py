from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from controlstock.models.EntryProduct import EntryProduct
from controlstock.templates.entry_product.EntryProductForm import EntryProductForm

# views.py

class EntryListView(ListView):
    model = EntryProduct
    template_name = 'entry_product/entry_product_list.html'
    context_object_name = 'entry_products'

class EntryCreateView(CreateView):
    model = EntryProduct
    form_class = EntryProductForm
    template_name = 'entry_product/entry_product_form.html'
    success_url = reverse_lazy('entry_list')

class EntryUpdateView(UpdateView):
    model = EntryProduct
    form_class = EntryProductForm
    template_name = 'entry_product/entry_product_form.html'
    success_url = reverse_lazy('entry_list')

class EntryDeleteView(DeleteView):
    model = EntryProduct
    template_name = 'entry_product/entry_product_delete.html'
    success_url = reverse_lazy('entry_list')
