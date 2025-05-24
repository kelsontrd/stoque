from django.apps import AppConfig


class ControlstockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'controlstock'
    
    def ready(self):
        import controlstock.models.signals.update_product
