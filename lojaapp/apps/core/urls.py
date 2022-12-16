from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]

app_name = 'categories'

urlpatterns = [
    path('/categories', views.categories, name='categories', verbose_name = 'Categorias'),
]

app_name = 'products'

urlpatterns = [
    path('/products', views.products, name='products', verbose_name = 'Produtos'),
]