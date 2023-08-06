from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from game.filters import GameFilters
from game.forms import GameForm, GameUpdateForm
from game.models import Game


class GameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'game/create_game.html'
    model = Game
    form_class = GameForm
    success_url = reverse_lazy('library')
    permission_required = 'game.add_game'

    def form_valid(self, form):
        if form.is_valid():
            game = form.save(commit=False)
            game.uploader = self.request.user
            game.save()
            return redirect(self.success_url)
        return super().form_valid(form)


class GameHomeView(ListView):
    template_name = 'game/store.html'
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

        user = self.request.user
        owned_games_ids = get_all_games.filter(users=user).values_list('id', flat=True)
        context['owned_games_ids'] = list(owned_games_ids)

        return context


class GameListView(LoginRequiredMixin, ListView):
    template_name = 'game/library.html'
    model = Game
    permission_required = 'game.view_game'

    def get_queryset(self):
        return Game.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_filters = GameFilters(self.request.GET, queryset=self.get_queryset())
        filtered_games = my_filters.qs
        context['all_games'] = self.get_queryset()
        context['uploaded_games'] = filtered_games.filter(uploaded=True)
        context['form_filters'] = my_filters.form

        user = self.request.user
        games = Game.objects.filter(users=user)
        game_count = games.count()
        context['library_games'] = games
        context['game_count'] = game_count

        return context


class GameUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'game/update_game.html'
    model = Game
    form_class = GameUpdateForm
    success_url = reverse_lazy('library')
    permission_required = 'game.change_game'


class GameDeteleView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'game/delete_game.html'
    model = Game
    success_url = reverse_lazy('library')
    permission_required = 'game.delete_game'


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'registration/profile.html'
    model = User

    def get_queryset(self):
        return Game.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        games = Game.objects.filter(users=user)
        game_count = games.count()
        context['game_count'] = game_count

        my_filters = GameFilters(self.request.GET, queryset=self.get_queryset())
        filtered_games = my_filters.qs
        uploaded_games_count = filtered_games.filter(uploaded=True).count()
        context['uploaded_games_count'] = uploaded_games_count

        return context


@login_required
def purchase_game(request, game_id):
    game = Game.objects.get(pk=game_id)
    user = request.user
    if game.users.filter(username=user.username).count() == 0:
        game.users.add(request.user)
        game.save()
        return redirect('library')
    else:
        return redirect('store')
