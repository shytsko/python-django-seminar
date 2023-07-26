import random
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def coin(request):
    result = random.choice(['орел', 'решка'])
    logger.info(f"coin: {result}")
    return HttpResponse(result)


def cube(request):
    result = random.randint(1, 6)
    logger.info(f"cube: {result}")
    return HttpResponse(result)


def number(request):
    result = random.randint(0, 100)
    logger.info(f"number: {result}")
    return HttpResponse(result)
