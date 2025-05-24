from django import forms
from controlstock.models.OutProduct import OutProduct
from controlstock.models.OperationDescription import OperationDescription

class OutProductForm(forms.ModelForm):
    class Meta:
        model = OutProduct
        fields = '__all__'
        widgets = {
            'operation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aplica 'form-control' a todos os campos
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()

        # Filtro específico para operation_description
        self.fields['operation_description'].queryset = OperationDescription.objects.filter(type_operation=False)
