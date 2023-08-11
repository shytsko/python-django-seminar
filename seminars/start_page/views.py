from django.shortcuts import render


def index(request):
    return render(request, 'start_page/index.html', {'title': 'Стартовая страница сайта'})
