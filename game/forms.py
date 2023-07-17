from django import forms
from django.forms import TextInput, NumberInput, DateInput, Textarea

from game.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        # fields = '__all__'
        fields = ['title', 'genre', 'developer', 'release_date', 'description', 'price']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Enter the game title', 'class': 'form-control'}),
            'genre': TextInput(attrs={'placeholder': 'Enter the game genre', 'class': 'form-control'}),
            'developer': TextInput(attrs={'placeholder': 'Enter the game developer', 'class': 'form-control'}),
            'release_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': Textarea(
                attrs={'placeholder': 'Enter the game description', 'class': 'form-control', 'rows': 3}),
            'price': NumberInput(attrs={'placeholder': 'Enter the game price', 'class': 'form=control'})

        }

    def clean(self):
        cleaned_data = self.cleaned_data
        check_games = Game.objects.filter(title=cleaned_data['title'])
        if check_games:
            msg = 'This game already exists on market library'
            self._errors['title'] = self.error_class([msg])


class GameUpdateForm(forms.ModelForm):
    class Meta:
        model = Game
        # fields = '__all__'
        fields = ['title', 'genre', 'developer', 'release_date', 'description', 'price']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Enter the game title', 'class': 'form-control'}),
            'genre': TextInput(attrs={'placeholder': 'Enter the game genre', 'class': 'form-control'}),
            'developer': TextInput(attrs={'placeholder': 'Enter the game developer', 'class': 'form-control'}),
            'release_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': Textarea(
                attrs={'placeholder': 'Enter the game description', 'class': 'form-control', 'rows': 3}),
            'price': NumberInput(attrs={'placeholder': 'Enter the game price', 'class': 'form=control'})

        }
