from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('game/coin/<int:count>/', views.coin, name='coin'),
    path('game/cube/<int:count>/', views.cube, name='cube'),
    path('game/number/<int:count>/', views.number, name='number'),
    path('articles/<int:author_id>', views.get_articles_by_author, name='get_articles_by_author'),
    path('article/<int:article_id>', views.article, name='article'),
]
