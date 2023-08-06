from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Название товара'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'placeholder': 'Описание товара'}))
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    count = forms.IntegerField(label='Количество', min_value=0)
    image = forms.ImageField(label='Изображение')


class ProductChangeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'count', 'image']
