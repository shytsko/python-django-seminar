from django.shortcuts import render, redirect
from .forms import SelectGameForm
import logging

logger = logging.getLogger(__name__)


def game_select(request):
    if request.method == 'POST':
        form = SelectGameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            logger.info(f'Получили {game=}, {count=}')
            return redirect(f'/seminar3/game/{game}/{count}/')
    else:
        form = SelectGameForm()
    return render(request, 'seminar4/game_select.html', {'form': form})
