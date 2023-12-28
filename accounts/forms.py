from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Regions, Speciality, Moderator_base


class LoginForm(forms.Form):
    email = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class ModeratorForm(forms.ModelForm):
    '''first_name = forms.CharField(label="Имя", max_length=100)
    second_name = forms.CharField(label="Фамилияя", max_length=100)
    middle_name = forms.CharField(label="Отчество", max_length=100)
    position = forms.ModelChoiceField(label="Регион присутствия", queryset=position.objects.all())
    phone_number = forms.CharField(label="Номер телефона", max_length=100)
    speciality = forms.ModelChoiceField(label="Специальность", queryset=speciality.objects.all())'''

    class Meta:
        model = Moderator_base
        fields = ['first_name', 'second_name', 'middle_name', 'subdivision', 'region', 'phone_number', 'post']