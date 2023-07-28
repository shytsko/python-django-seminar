import random
import logging

from django.http import HttpResponse, JsonResponse
from task5app.models import Coin

logger = logging.getLogger(__name__)


def coin(request):
    result = Coin(result=random.choice(['орел', 'решка']))
    result.save()
    logger.info(f"coin: {result}")
    return HttpResponse(result)


def coin_statistic(request):
    return JsonResponse(Coin.get_statistic(20))


def cube(request):
    result = random.randint(1, 6)
    logger.info(f"cube: {result}")
    return HttpResponse(result)


def number(request):
    result = random.randint(0, 100)
    logger.info(f"number: {result}")
    return HttpResponse(result)
