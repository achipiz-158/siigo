from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'list_prince',
            'id_tenant',
        ]
        labels = {
            'name': 'nombre',
            'description': 'Descripcion',
            'list_prince': 'Precio',
            'id_tenant': 'Inquilino',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'autofocus': 'autofocus',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'autofocus': 'autofocus',
                }
            ),
            'list_prince': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'autofocus': 'autofocus',
                }
            ),
            'id_tenant': forms.Select(
                attrs={
                    'class': "form-control",
                    'autofocus': 'autofocus',
                }
            ),
        }