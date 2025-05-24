from django.contrib import admin
from controlstock.models import Product, Customer, OutProduct, OperationDescription, Unity, EntryProduct

admin.site.register(Product.Product)
admin.site.register(Customer.Customer)
admin.site.register(OutProduct.OutProduct)
admin.site.register(OperationDescription.OperationDescription)
admin.site.register(Unity.Unity)
admin.site.register(EntryProduct.EntryProduct)

