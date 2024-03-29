# Generated by Django 2.1 on 2019-11-06 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_date', models.CharField(max_length=100)),
                ('doc_number', models.CharField(max_length=100)),
                ('total_tax', models.IntegerField()),
                ('total_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('unit_value', models.FloatField()),
                ('item_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('list_prince', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='id_tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Tenant'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Product'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='id_tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Tenant'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='id_invoice_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.InvoiceItem'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='id_tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Tenant'),
        ),
    ]
