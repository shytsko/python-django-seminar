from django import forms
from seminar2_task3_app.models import Author


class SelectGameForm(forms.Form):
    GAME_CHOICES = [
        ('coin', 'Бросить монету'),
        ('cube', 'Бросить кубик'),
        ('number', 'Случайный номер'),
    ]
    game = forms.ChoiceField(choices=GAME_CHOICES)
    count = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    biography = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Биография'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Заголовок'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Текст статьи'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Катагория'}))


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Текст комментария'}))
