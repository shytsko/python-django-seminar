from django.contrib import admin
from .models import Author, Article, Comment
from django.utils import timezone


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']
    ordering = ['firstname']


def publish(modeladmin, request, queryset):
    queryset.update(is_published=True, publication_date=timezone.now())


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['publication_date', 'author', 'category', 'is_published']
    search_fields = ['content']
    actions = [publish]
    fields = ['title', 'content', 'publication_date', 'author', 'category', 'views', 'is_published']
    readonly_fields = ['publication_date', 'views', 'is_published']


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['author', 'article', 'date_create']
    search_fields = ['text']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
