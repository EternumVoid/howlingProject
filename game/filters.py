import django_filters

from game.models import Game


class GameFilters(django_filters.FilterSet):
    # list_of_games = [((game.title, game.title.upper())) for game in Game.objects.filter(active=True)]
    # title = django_filters.ChoiceFilter(choices=list(set(list_of_games)))

    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    # genre = django_filters.CharFilter(lookup_expr='icontains', label='Genre')

    class Meta:
        model = Game
        fields = ['title']
        # 'genre'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['title'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the game title'})
        # self.filters['genre'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the game genre'})




