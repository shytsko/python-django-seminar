from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, ProductChangeForm
from .models import Product
import logging

logger = logging.getLogger(__name__)


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            logger.info(f'Получили {form.cleaned_data=}')

            new_product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                count=count,
                image=image,
            )
            logger.info(f'Создан объект {new_product}')
            message = 'Товар сохранёна'
        else:
            message = 'Ошибка в данных'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'homework4/product_add.html', {'form': form, 'message': message})


def product_change(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductChangeForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            message = 'Товар обновлен'
        else:
            message = 'Ошибка в данных'
    else:
        form = ProductChangeForm(instance=product)
        message = 'Заполните форму'
    return render(request, 'homework4/product_change.html', {'form': form, 'message': message})
