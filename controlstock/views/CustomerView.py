from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from controlstock.models.Customer import Customer
from controlstock.templates.customer.CustomerForm import CustomerForm

# views.py

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = reverse_lazy('customer_list')
