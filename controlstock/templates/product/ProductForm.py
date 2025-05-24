from django import forms
from controlstock.models.Product import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Ou especifique os campos desejados
