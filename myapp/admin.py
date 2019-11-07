from django.contrib import admin
from import_export.admin import ImportExportMixin
from myapp.resource import ProductResource
from .models import Customer, Product, Invoice, InvoiceItem, Tenant


class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProductResource


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Tenant)
