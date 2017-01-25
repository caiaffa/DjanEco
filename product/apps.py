from django.apps import AppConfig
from watson import search as watson

class ProductConfig(AppConfig):
    name = 'product'
    verbose_name = 'Produto'

    def ready(self):
        Product = self.get_model('Product')
        watson.register(Product)