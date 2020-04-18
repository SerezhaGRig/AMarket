from django.urls import path, include
from .views import index, prod_table, add, delete


app_name = 'market'
urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('delete/', delete, name='del'),
    path('<str:cat_name>', prod_table),
]
