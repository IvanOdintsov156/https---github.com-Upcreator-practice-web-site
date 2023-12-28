from django import forms
from .models import students
from accounts.models import Moderator_base

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['practice', 'full_name', 'email', 'phone_number']

    labels = {
        'practice': 'Направление практики',
        'full_name': 'ФИО',
        'email': 'Почта',
        'phone_number': 'Номер телефона',
    }

    widgets = {
        'practice': forms.Select(attrs={'class': 'custom-input'}),
        'full_name': forms.TextInput(attrs={'class': 'custom-input'}),
        'email': forms.EmailInput(attrs={'class': 'custom-input'}),
        'phone_number': forms.TextInput(attrs={'class': 'custom-input'}),
        'status': forms.Select(attrs={'class': 'custom-input'}),
    }

class StatusChangeForm(forms.ModelForm):
    model = students
    fields = ['status', 'practice', 'full_name', 'email', 'phone_number']
    labels = {
        'status': 'Статус',
        'practice': 'Выбранная практика',
        'full_name': 'ФИО',
        'email': 'Почта',
        'phone_number': 'Номер телефона',
    }
    class Meta:
        model = students
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=[("отклонено", "Отклонено"), ("принято", "Принято")]),
        }