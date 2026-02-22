# django
Django Tutorial

## 0. Prerequisites
Python installed

## 1. Create env
```
python -m venv .venv
source .venv/bin/activate
```

## 2. Install django
```
pip3 install django
```

## 3. Create project
```
django-admin startproject config .
```

## 4. Create app products
```
./manage.py startapp products
```

## 5. Create products/models.py
```
echo "from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(\"person's first name\", max_length=30)
" > products/models.py    
```

## 6. Add products to main url and INSTALLED_APPS
```
sed -ri "s/urlpatterns = \[/urlpatterns = \[\n    path('',views.index),\n    path('products\/', include('products.urls')),/g" config/urls.py
sed -ri "s/from django.urls import path/from django.urls import path, include\nfrom . import views/" config/urls.py
sed -ri "s/INSTALLED_APPS = \[/INSTALLED_APPS = \[\n    'products',/" config/settings.py
sed -ri "s/'DIRS': \[\],/'DIRS': \[os.path.join(BASE_DIR, 'config\/templates')\],/" config/settings.py
sed -ri "s/from pathlib import Path/from pathlib import Path\nimport os/" config/settings.py

```
## 7. Create config/views.py
```
echo "from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,
        'root.html',
        {
            'title': 'title',
            'bodystart': 'bodystart',
            'bodystop': 'bodystop',
        }
    )
" > config/views.py 
```

## 8. Create root.html
```
mkdir config/templates
echo "<html>
<title> {{ title }}</title>

<body>
  {{ bodystart }}
    <h2><a href=products/>products</a></h2>
    <h2><a href=admin/>admin</a></h2>
  {{ bodystop }}
</body>
</html>
" > config/templates/root.html
```

## 9. Create products/urls.py
```
echo "from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.index)
]" > products/urls.py
```

## 10. Create products/views.py
```
echo "from django.http import HttpResponse
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
" > products/views.py 
```

## 11. Create db for products
```
./manage.py makemigrations products
./manage.py migrate 
```
## 12. Create superuser
```
./manage.py createsuperuser --username admin --email admin@example.com
```

## 13. Create index.html
```
mkdir products/templates
echo "<html>
<title> {{ title }}</title>

<body>
  {{ bodystart }}
  <table border=1>
  <tr>
    <th>ID</th>
    <th>NAME</th>
  </tr>
  {% for product in products %}
    <tr>
      <td>{{ product.id }}</td>
      <td>{{ product.name }}</td>
    </tr>
  {% endfor %}
  </table>
  {{ bodystop }}
</body>
</html>
" > products/templates/index.html
```

## 14. Run server
```
./manage.py runserver
```