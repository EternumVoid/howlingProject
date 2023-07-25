from random import randint

from django.contrib.auth import models, get_user_model
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from howlingProject.forms import CustomUserCreationForm
from howlingProject.settings import EMAIL_HOST_USER
from user.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'registration/create_user.html'
    # model = User
    # form_class = UserForm
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home_page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = Group.objects.all()
        return form

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)  # salvam datele in tabela auth_user
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()

            # new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{randint(100, 999)}'

            new_user.save()

            group = form.cleaned_data['category']
            group.user_set.add(new_user)

            # trimiterea de mail fara template
            subject = 'Confirmare cont nou!'
            message = f'Salut, {new_user.first_name} {new_user.last_name}. Numele tau de utilzator este: {new_user.username}'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # trimiterea de mail cu template
            # details_user = {
            #     'fullname': f'{new_user.first_name} {new_user.last_name}',
            #     'username': new_user.username
            # }
            # subject = 'Confirmare cont nou in aplicatie'
            # message = get_template('mail.html').render(details_user)
            # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            # mail.content_subtype = 'html'
            # mail.send()

        return super().form_valid(form)
