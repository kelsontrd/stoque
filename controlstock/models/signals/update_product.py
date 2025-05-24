from django.db.models.signals import post_save
from django.dispatch import receiver
from controlstock.models.OutProduct import OutProduct
from controlstock.models.EntryProduct import EntryProduct

@receiver(post_save, sender=OutProduct)
def update_product_stock_out(sender, instance, created, **kwargs):
    if created:
        instance.adjust_stock()

@receiver(post_save, sender=EntryProduct)
def update_product_stock_entry(sender, instance, created, **kwargs):
    if created:
        instance.adjust_stock()