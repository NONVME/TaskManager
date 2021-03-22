from .models import Tasks
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext as _


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'author', 'executor']
