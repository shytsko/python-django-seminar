from django.shortcuts import render, redirect, get_object_or_404
from .forms import SelectGameForm, AuthorForm, ArticleForm, CommentForm
import logging
from seminar2_task3_app.models import Author, Article, Comment

logger = logging.getLogger(__name__)


def game_select(request):
    if request.method == 'POST':
        form = SelectGameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            logger.info(f'Получили {game=}, {count=}')
            return redirect(f'/seminar3/game/{game}/{count}/')
    else:
        form = SelectGameForm()
    return render(request, 'seminar4/game_select.html', {'form': form})


def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthdate = form.cleaned_data['birthdate']
            logger.info(f'Получили {form.cleaned_data=}')
            new_author = Author.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                biography=biography,
                birthdate=birthdate
            )
            logger.info(f'Создан объект {new_author}')
            message = 'Пользователь сохранён'
        else:
            message = 'Ошибка в данных'
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'seminar4/author_add.html', {'form': form, 'message': message})


def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            logger.info(f'Получили {form.cleaned_data=}')

            new_article = Article.objects.create(
                title=title,
                content=content,
                author=author,
                category=category,
            )
            logger.info(f'Создан объект {new_article}')
            message = 'Статья сохранёна'
        else:
            message = 'Ошибка в данных'
    else:
        form = ArticleForm()
        message = 'Заполните форму'
    return render(request, 'seminar4/article_add.html', {'form': form, 'message': message})


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            logger.info(f'Получили {form.cleaned_data=}')

            new_comment = Comment.objects.create(
                author=comment_author,
                article=article,
                text=comment_text,
            )
            logger.info(f'Создан объект {new_comment}')
    else:
        form = CommentForm()
    context = {
        'title': article.title,
        'article': article,
        'comments': comments,
        'form': form
    }
    return render(request, 'seminar4/article.html', context)
