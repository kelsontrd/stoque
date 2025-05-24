from django.urls import path
from django.views.generic import RedirectView
from controlstock.views.HomeView import HomeView
from controlstock.views.ProductView import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from controlstock.views.CustomerView import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from controlstock.views.EntryView import EntryListView, EntryCreateView, EntryUpdateView, EntryDeleteView
from controlstock.views.OutView import OutProductListView, OutProductCreateView, OutProductUpdateView, OutProductDeleteView
from controlstock.views.reports.product.ProductReportView import ProductReportView
from controlstock.views.reports.product.ProductPdfView import ProductPdfView
from controlstock.views.reports.out.OutCustomertReportView import OutCustomerReportView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('entry/', EntryListView.as_view(), name='entry_list'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
    path('out/', OutProductListView.as_view(), name='out_product_list'),
    path('out/new/', OutProductCreateView.as_view(), name='out_product_create'),
    path('out/<int:pk>/edit/', OutProductUpdateView.as_view(), name='out_product_update'),
    path('out/<int:pk>/delete/', OutProductDeleteView.as_view(), name='out_product_delete'),
    path('reports/products/', ProductReportView.as_view(), name='product_report'),
    path('reports/products/pdf/', ProductPdfView.as_view(), name='product_report_pdf'),
    path('reports/out/', OutCustomerReportView.as_view(), name='out_product_customer_report'),


]