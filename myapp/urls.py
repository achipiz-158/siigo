from django.urls import path
from .views import importar

urlpatterns = [

    path('import', importar, name='import'),

]
