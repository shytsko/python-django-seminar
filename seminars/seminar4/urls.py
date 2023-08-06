from django.urls import path
from . import views

urlpatterns = [
    path('game/select/', views.game_select, name='game_select'),
    path('author/add/', views.author_add, name='author_add'),
    path('article/add/', views.article_add, name='article_add'),
    path('article/<int:article_id>', views.get_article, name='get_article'),
]
