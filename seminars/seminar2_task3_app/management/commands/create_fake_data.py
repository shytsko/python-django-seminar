from django.core.management.base import BaseCommand
from seminar2_task3_app.models import Author, Article, Comment
from random import randint, choice
from datetime import date


class Command(BaseCommand):
    help = "Create test data"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of authors')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        authors = [
            Author(
                firstname=f'Author{i}',
                lastname=f'Author{i}',
                email=f'author{i}@mail.com',
                biography="Quisque gravida enim at nibh tincidunt commodo. Integer rutrum velit eget varius cursus",
                birthdate=date(year=randint(1950, 2000), month=randint(1, 12), day=randint(1, 28))
            )
            for i in range(1, count + 1)
        ]

        for author in authors:
            author.save()

        articles = [
            Article.add(
                title=f"Article {i} by the author {author.fullname}",
                content="Quisque gravida enim at nibh tincidunt commodo. Integer rutrum velit eget varius cursus",
                author=author,
                category="category"
            )
            for author in authors
            for i in range(1, count + 1)

        ]

        for article in articles:
            article.save()

        comments = []
        for i in range(1, count * 10):
            author = choice(authors)
            article = choice(articles)
            comments.append(
                Comment(
                    author=author,
                    article=article,
                    text=f"Сomment on the article '{article.title}' from the {author.fullname}"
                )
            )

        for comment in comments:
            comment.save()
