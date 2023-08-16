import random
import logging
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from task5app.models import Coin

logger = logging.getLogger(__name__)


def coin(request, count):
    for _ in range(count):
        result = Coin.throw()
        logger.info(f"coin: {result}")
    return HttpResponse(f"Монета брошена {count} раз")


def coin_statistic(request, number_latter):
    context = {
        'data': Coin.get_statistic(number_latter)
    }
    return render(request, 'task5app/statistic.html', context)


def cube(request):
    result = random.randint(1, 6)
    logger.info(f"cube: {result}")
    return HttpResponse(result)


def number(request):
    result = random.randint(0, 100)
    logger.info(f"number: {result}")
    return HttpResponse(result)
