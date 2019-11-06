from django.shortcuts import render
from tablib import Dataset


def importar(request):
    # template = loader.get_template('export/import.html')
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
    return render(request, 'export/import.html')
