from django.urls import path
from django.conf.urls import url

from myapp import views
from .views import importar, ProductCreate, ProductUpdate, ProductList, ProductDetail

urlpatterns = [

    path('import', importar, name='import'),
    path('SuggestProduct/', views.ajax_load_product, name='ajax_load_product'),
    path('searchtest/', views.searchProduct, name='searchProduct'),

    # URLS PRODUCT
    url(r'^create_product$', ProductCreate.as_view(), name="product_create"),
    url(r'list_product', ProductList.as_view(), name="product_list"),
    url(r'^edit_product/(?P<pk>\d+)/$', ProductUpdate.as_view(), name='product_edit'),
    url(r'^detail_product/(?P<pk>.+)/$', ProductDetail.as_view(), name='product_detail'),

]
