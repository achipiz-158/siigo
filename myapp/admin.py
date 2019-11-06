from django.contrib import admin

# Register your models here.

from .models import Customer, Product, Invoice, InvoiceItem, Tenant


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Tenant)
