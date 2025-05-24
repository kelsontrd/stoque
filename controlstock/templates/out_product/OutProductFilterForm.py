from django import forms
from controlstock.models.Product import Product
from controlstock.models.Customer import Customer
from controlstock.models.OutProduct import OutProduct

class OutProductFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data inicial"
    )
    end_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data final"
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), required=False, label="Produto"
    )
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(), required=False, label="Cliente"
    )
