from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ADMIN
from django.contrib.auth.models import User
from accounts.models import Regions, Speciality, Moderator_base

class SignUpForm(UserCreationForm):
    telephone_number = forms.CharField(
        max_length=15,
        help_text='Номер телефона. Формат +7910...', label='test'
    )
    user_post = forms.CharField(
        max_length=50,
        help_text='Должность', label='test'
    )

    structural_subdivision = forms.CharField(
        max_length=100,
        help_text='Структурное подразделение', label='test'
    )

    region = forms.ModelChoiceField(queryset=Regions.objects.all(),
        help_text='Место пребывания', label='test'
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Одна большая буква и т.д.',
    )

    class Meta:
        model = ADMIN
        fields = ('user_name', 'first_name', 'last_name', 'e_mail', 'telephone_number', 'password1', 'password2', 'user_post', 'structural_subdivision', 'region')