from import_export import resources
from .models import Product


class PersonaResource(resources.ModelResource):
    class Meta:
        model = Product
