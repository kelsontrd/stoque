from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from controlstock.models.Product import Product  # ajuste para seu caminho real
import io

class ProductPdfView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="relatorio_produtos.pdf"'

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)

        styles = getSampleStyleSheet()
        elements = []

        # Título
        elements.append(Paragraph("Relatório de Produtos", styles['Title']))
        elements.append(Spacer(1, 0.5 * cm))

        # Data de geração
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        elements.append(Paragraph(f"Gerado em: {data_atual}", styles['Normal']))
        elements.append(Spacer(1, 0.5 * cm))

        # Dados dos produtos
        products = Product.objects.all()

        data = [["Nome do Produto", "Quantidade em Estoque"]]
        for produto in products:
            data.append([produto.name, str(produto.quantity)])

        # Tabela
        table = Table(data, colWidths=[10 * cm, 5 * cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
