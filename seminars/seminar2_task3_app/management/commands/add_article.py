from django.core.management.base import BaseCommand
from seminar2_task3_app.models import Author, Article


class Command(BaseCommand):
    help = "Add new article"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('author_id', type=int)
        parser.add_argument('category', type=str)

    def handle(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.filter(pk=author_id).first()
        if author is not None:
            new_article = Article.add(title=kwargs.get('title'),
                                      content=kwargs.get('content'),
                                      author=author,
                                      category=kwargs.get('category'))
            self.stdout.write(f'{new_article}')
