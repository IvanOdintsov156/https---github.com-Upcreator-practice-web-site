from django import forms
from .models import Practice

class PracticeCreateForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ['name_of_PSK_or_structure', 'region', 'practice_director_full_name', 'need_amount_of_practicants', 'practice_description', 'required_skills', 'start_date', 'end_date', 'direction']
        widgets = {
        'name_of_PSK_or_structure': forms.TextInput(attrs={'class': 'custom-input'}),
        'start_date': forms.DateInput(attrs={'type': 'date'}),
        'end_date': forms.DateInput(attrs={'type': 'date'}),
        'need_amount_of_practicants': forms.NumberInput(attrs={'class': 'custom-input'}),
        'practice_description': forms.Textarea(attrs={'class': 'custom-input'}),
        'required_skills': forms.Textarea(attrs={'class': 'custom-input'}),
        'practice_director_full_name': forms.TextInput(attrs={'class': 'custom-input'}),
        
    }

class PracticeEditForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ['name_of_PSK_or_structure', 'region', 'practice_director_full_name', 'need_amount_of_practicants', 'practice_description', 'required_skills', 'start_date', 'end_date', 'direction']
        widgets = {
            'name_of_PSK_or_structure': forms.TextInput(attrs={'class': 'custom-input'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'need_amount_of_practicants': forms.NumberInput(attrs={'class': 'custom-input'}),
            'practice_description': forms.Textarea(attrs={'class': 'custom-input'}),
            'required_skills': forms.Textarea(attrs={'class': 'custom-input'}),
            'practice_director_full_name': forms.TextInput(attrs={'class': 'custom-input'}),
        }