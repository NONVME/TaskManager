from .models import User
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'full_name']
        widgets = {
            'user_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите user name'
            }),
            'full_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полнок имя',
            }),
        }
