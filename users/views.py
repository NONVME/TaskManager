from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import UserAuthenticationForm, UserRegisterForm
from .models import CustomUser


def get_users(request):
    users = CustomUser.objects.order_by('-id')
    return render(request, 'users/users.html', {
        'title': _('Список пользователей'),
        'users': users
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _('Вы успешно зарегестрированны'))
            return redirect('users')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _('Вы успешно авторизовались'))
            return redirect('home')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = UserAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, _('Вы разлогинены'))
    return redirect('home')


def update(request, pk):
    pass


def delete(request, pk):
    pass
