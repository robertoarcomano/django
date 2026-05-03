from django.urls import path
from . import views
from .views import product, success

urlpatterns = [
    path('', views.index),
    path('new/', views.index),
    path('product/', product, name='product'),
    path('success/', success, name='success'),  # 👈 questa mancava
]