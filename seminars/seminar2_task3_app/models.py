from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    biography = models.TextField()
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.fullname}"

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"title: {self.title}, author: {self.author.fullname}"

    @staticmethod
    def add(title, content, author, category):
        new_article = Article(title=title, content=content, author=author, category=category)
        new_article.save()
        return new_article

    @staticmethod
    def get(id_article):
        article = Article.objects.filter(pk=id_article).first()
        return article

    @staticmethod
    def update(id_article, title=None, content=None, author=None, category=None):
        article = Article.objects.filter(pk=id_article).first()
        if article is not None:
            if title:
                article.title = title
            if content:
                article.content = content
            if author:
                article.author = author
            if category:
                article.category = category
        article.save()
        return article

    @staticmethod
    def remove(id_article):
        article = Article.objects.filter(pk=id_article).first()
        if article is not None:
            article.delete()

    @staticmethod
    def get_by_author_name(author_name):
        author = Author.objects.filter(firstname=author_name).first()
        if author is not None:
            articles = Article.objects.filter(author=author)
            return articles
        return None


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment for article '{self.article.title}'; author: {self.author.fullname}"

    @staticmethod
    def get_by_author_name(author_name):
        author = Author.objects.filter(firstname=author_name).first()
        if author is not None:
            comments = Comment.objects.filter(author=author)
            return comments
        return None

    @staticmethod
    def get_by_article_title(article_title):
        article = Article.objects.filter(title=article_title).first()
        if article is not None:
            articles = Comment.objects.filter(article=article)
            return articles
        return None
