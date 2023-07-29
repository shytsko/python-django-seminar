from django.core.management.base import BaseCommand
from seminar2_task3_app.models import Author, Article


class Command(BaseCommand):
    help = "Update article"

    def add_arguments(self, parser):
        parser.add_argument('id_article', type=int, help='User ID')
        parser.add_argument('--title', type=str)
        parser.add_argument('--content', type=str)
        parser.add_argument('--author_id', type=int)
        parser.add_argument('--category', type=str)

    def handle(self, *args, **kwargs):
        id_article = kwargs.get('id_article')
        title = kwargs.get('title')
        content = kwargs.get('content')
        author_id = kwargs.get('author_id')
        author = Author.objects.filter(pk=author_id).first()
        category = kwargs.get('category')

        article = Article.update(id_article=id_article, title=title, content=content, author=author, category=category)
        self.stdout.write(f'{article}')
