from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import BaseFormView

from game.filters import GameFilters
from game.forms import GameForm, GameUpdateForm
from game.models import Game


class GameHomeView(ListView):
    template_name = 'game/store.html'
    model = Game
    context_object_name = 'all_games'


class GameCreateView(CreateView):
    template_name = 'game/create_game.html'
    model = Game
    form_class = GameForm
    success_url = reverse_lazy('list-of-games')


class GameListView(ListView):
    template_name = 'game/list_of_games.html'
    model = Game
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_all_games = Game.objects.filter(active=True)
        my_filters = GameFilters(self.request.GET, queryset=get_all_games)
        get_all_games = my_filters.qs
        context['all_games'] = get_all_games
        context['form_filters'] = my_filters.form
        return context


class GameUpdateView(UpdateView):
    template_name = 'game/update_game.html'
    model = Game
    form_class = GameUpdateForm
    success_url = reverse_lazy('list-of-games')


class GameDeteleView(DeleteView):
    template_name = 'game/delete_game.html'
    model = Game
    success_url = reverse_lazy('list-of-games')
