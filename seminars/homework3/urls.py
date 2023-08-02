from django.urls import path
from . import views

urlpatterns = [
    path('customer/<int:customer_id>/orders/', views.CustomerOrders.as_view(), name='customer_orders'),
    path('customer/<int:customer_id>/products/<int:prev_days>/', views.CustomerProducts.as_view(),
         name='customer_products'),
]
