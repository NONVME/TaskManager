from .models import Statuses
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext as _


class StatusesForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Введите новое название статуса'),
            })
        }
