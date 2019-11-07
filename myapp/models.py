from django.db import models
from django.conf import settings


class Tenant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    list_prince = models.FloatField()
    id_tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class InvoiceItem(models.Model):
    quantity = models.FloatField()
    unit_value = models.FloatField()
    item_value = models.FloatField()
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    id_tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)


class Invoice(models.Model):
    doc_date = models.CharField(max_length=100)
    doc_number = models.CharField(max_length=100)
    total_tax = models.IntegerField()
    total_value = models.IntegerField()
    id_invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.PROTECT)
    id_tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
