from django.http import HttpResponse
from products.models import Product
from django.shortcuts import render

products = []
for i in range(1,10):
    products.append({'id': i, 'name': 'name'+str(i)})

def index(request):
    product = Product.objects.first()
    if product:
        print(product.name)
    else:
        product = Product()
        product.id=1
        product.name='name1'
        product.save()
    return render(request,
        'index.html',
        {
            'title': 'title',
            'bodystart': 'bodystart',
            'products': Product.objects.all(),
            'bodystop': 'bodystop',
        }
    )

