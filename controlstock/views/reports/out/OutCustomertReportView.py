from django.views.generic import TemplateView
from controlstock.models.Customer import Customer
from controlstock.services.out_product.OutReport import OutReport

class OutCustomerReportView(TemplateView):
    template_name = 'out_product/out_customer_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = Customer.objects.all()
        cliente_id = self.request.GET.get('cliente')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')

        saidas = []
        cliente = None
        if cliente_id:
            saidas = OutReport.por_cliente(cliente_id, data_inicio, data_fim)
            cliente = Customer.objects.filter(id=cliente_id).first()

        context.update({
            'clientes': clientes,
            'cliente_selecionado': cliente_id,
            'cliente': cliente,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'saidas': saidas,
        })
        return context