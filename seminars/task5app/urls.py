from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:count>/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
    path('coin_statistic/<int:number_latter>', views.coin_statistic, name='coin_statistic'),
]
