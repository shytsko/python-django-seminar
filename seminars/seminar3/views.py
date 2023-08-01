from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from seminar2_task3_app.models import Author, Article, Comment


def home(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'seminar3/home.html', context)


def about(request):
    context = {
        'title': 'Обо мне'
    }
    return render(request, 'seminar3/about.html', context)


def coin(request, count):
    context = {
        'title': 'Монетка',
        'attempts': [random.choice(['орел', 'решка']) for _ in range(count)]
    }
    return render(request, 'seminar3/game.html', context)


def cube(request, count):
    context = {
        'title': 'Кубик',
        'attempts': [random.randint(1, 6) for _ in range(count)]
    }
    return render(request, 'seminar3/game.html', context)


def number(request, count):
    context = {
        'title': 'Случайный номер',
        'attempts': [random.randint(0, 100) for _ in range(count)]
    }
    return render(request, 'seminar3/game.html', context)


def get_articles_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author)

    context = {
        'title': 'Статьи автора',
        'author': author,
        'articles': articles
    }
    return render(request, 'seminar3/articles.html', context)


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # author = article.author
    comments = Comment.objects.filter(article=article)

    context = {
        'title': article.title,
        'article': article,
        'comments': comments
    }
    return render(request, 'seminar3/article.html', context)
