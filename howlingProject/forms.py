from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


# custom file so i can overwrite the UserCreationForm and implement the 'category' field

class CustomUserCreationForm(UserCreationForm):
    category = forms.ModelChoiceField(queryset=Group.objects.all())
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('category',)
