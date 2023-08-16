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
        # last_results = Coin.objects.order_by("-date_time")[:count_last]
        # counter = {Coin.CoinSide.REVERSE: 0, Coin.CoinSide.OBVERSE: 0}
        # for result in last_results:
        #     counter[result.result] += 1
        # statistics = {Coin.CoinSide.REVERSE: counter[Coin.CoinSide.REVERSE] / count_last,
        #               Coin.CoinSide.OBVERSE: counter[Coin.CoinSide.OBVERSE] / count_last}
        # return statistics

        last_results = list(Coin.objects.values_list("id", flat=True).order_by("-date_time")[:count_last])
        statistic_data = (Coin.objects.filter(id__in=last_results)
                          .values('result')
                          .annotate(count=Count('result')))
        return {item['result']: item['count'] / count_last for item in statistic_data}

    def __str__(self):
        return self.result
