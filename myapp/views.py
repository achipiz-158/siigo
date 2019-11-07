import json
from django.shortcuts import render
from tablib import Dataset
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Product
from .forms import ProductForm
from .resource import ProductResource
from django.shortcuts import render


def export(request):
    product_resource = ProductResource()
    dataset = product_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    return response


def importar(request):
    # template = loader.get_template('import.html')
    if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        # print(dataset)
        nuevos_products = request.FILES['xlsfile']
        # print(nuevos_products)
        imported_data = dataset.load(nuevos_products.read())
        # print(dataset)
        result = product_resource.import_data(dataset, dry_run=True)  # Probar importacion de datos
        # print(result.has_errors())
        if not result.has_errors():
            product_resource.import_data(dataset, dry_run=False)  # Importando ahora
    return render(request, 'api/import.html')


def ajax_load_product(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        products = Product.objects.filter(name__istartswith=q)[:8]
        results = []
        for product in products:
            product_json = {'id': product.id, 'value': product.name, 'label': product.name}
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def searchProduct(request):
    template = 'api/search.html'
    return render(request, template)


class ProductList(ListView):
    model = Product
    template_name = 'api/list_product.html'
    context_object_name = 'products'


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'api/form_product.html'
    success_url = reverse_lazy('product_list')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'api/form_product.html'
    success_url = reverse_lazy('product_list')


class ProductDetail(DetailView):
    model = Product
    template_name = 'api/product_detail.html'
