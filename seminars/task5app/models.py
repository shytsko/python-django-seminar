import random
from enum import StrEnum
from django.db import models
from django.db.models import Count


class Coin(models.Model):
    class CoinSide(StrEnum):
        OBVERSE = 'obverse'
        REVERSE = 'reverse'

    result = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def throw(cls):
        result = random.choice(list(cls.CoinSide))
        cls(result=result).save()
        return result

    @staticmethod
    def get_statistic(count_last: int):
        statistic_data = (
            Coin.objects.order_by("-date_time")[:count_last].
            values('result').
            annotate(count=Count('result'))
        )
        return {item['result']: item['count'] / count_last for item in statistic_data}

    def __str__(self):
        return self.result
