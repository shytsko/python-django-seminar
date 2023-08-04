from django.urls import path
from . import views

urlpatterns = [
    path('game/select/', views.game_select, name='game_select'),
]
