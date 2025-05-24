from django import forms
from controlstock.models.EntryProduct import EntryProduct
from controlstock.models.OperationDescription import OperationDescription

class EntryProductForm(forms.ModelForm):
    class Meta:
        model = EntryProduct
        fields = '__all__'  # Ou especifique os campos desejados

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['OperationDescription'].queryset = OperationDescription.objects.filter(type_operation=True)
        self.fields['operation_description'].queryset = OperationDescription.objects.filter(type_operation=True)