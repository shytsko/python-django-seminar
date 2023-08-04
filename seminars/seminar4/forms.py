from django import forms


class SelectGameForm(forms.Form):
    GAME_CHOICES = [
        ('coin', 'Бросить монету'),
        ('cube', 'Бросить кубик'),
        ('number', 'Случайный номер'),
    ]
    game = forms.ChoiceField(choices=GAME_CHOICES)
    count = forms.IntegerField(min_value=1, max_value=64)
