from django.db import models
from django.db.models import Count


class Coin(models.Model):
    result = models.CharField(max_length=5)
    date_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_statistic(count_last: int):
        last_results = Coin.objects.order_by("-date_time")[:count_last]
        counter = {'орел': 0, 'решка': 0}
        for result in last_results:
            counter[result.result] += 1
        statistics = {'орел': counter['орел'] / count_last, 'решка': counter['решка'] / count_last}
        return statistics

        # statistic_data = Coin.objects.order_by("-date_time")[:count_last].values('result').annotate(count=Count('result'))
        # return {item['result']: item['count'] / count_last for item in statistic_data}

    def __str__(self):
        return self.result
