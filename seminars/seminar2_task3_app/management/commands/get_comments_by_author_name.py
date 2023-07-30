from django.core.management.base import BaseCommand
from seminar2_task3_app.models import Comment


class Command(BaseCommand):
    help = "Get comments by author name"

    def add_arguments(self, parser):
        parser.add_argument('author_name', type=str, help='author name')

    def handle(self, *args, **kwargs):
        author_name = kwargs.get('author_name')
        comments = Comment.get_by_author_name(author_name)
        self.stdout.write(f'{comments}')
