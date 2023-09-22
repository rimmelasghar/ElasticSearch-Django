from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Products

@registry.register_document
class ProductInventoryDocument(Document):

    class Index:
        name = "productinventory"

    class Django:
        model = Products
        fields = ['id', 'title', 'description']  
