from django import forms
from controlstock.models.Customer import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # Ou especifique os campos desejados
