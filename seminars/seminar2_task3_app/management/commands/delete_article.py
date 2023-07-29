from django.core.management.base import BaseCommand
from seminar2_task3_app.models import Author, Article


class Command(BaseCommand):
    help = "Delete article"

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        article_id = kwargs.get('article_id')
        article = Article.remove(article_id)
