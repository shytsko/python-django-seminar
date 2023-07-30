from django.core.management.base import BaseCommand
from seminar2_task3_app.models import Comment


class Command(BaseCommand):
    help = "Get comments by article title"

    def add_arguments(self, parser):
        parser.add_argument('article_title', type=str, help='article title')

    def handle(self, *args, **kwargs):
        article_title = kwargs.get('article_title')
        comments = Comment.get_by_article_title(article_title)
        self.stdout.write(f'{comments}')
