from django.urls import path
from . import views

urlpatterns = [
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:product_id>/change/', views.product_change, name='product_change'),
]
