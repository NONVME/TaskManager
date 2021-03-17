from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import UserRegisterForm


def users(request):
    users = User.objects.order_by('-id')
    return render(request, 'users/users.html', {
        'title': _('Список пользователей'),
        'users': users
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Вы успешно зарегестрированны'))
            return redirect('users')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    return render(request, 'users/login.html')


def update(request, pk):
    pass


def delete(request, pk):
    pass
