from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import MyUserChangeForm, UserAuthenticationForm, UserRegisterForm
from .models import CustomUser


def get_users(request):
    users = CustomUser.objects.order_by('-pk')
    return render(request, 'users/users.html', {
        'title': _('Список пользователей'),
        'users': users
    })


def user_register(request):
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


@login_required(login_url='/login/')
def user_change(request, pk):
    if request.method == 'POST':
        form = MyUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Изменения внесены'))
            return redirect('users')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = MyUserChangeForm(instance=request.user)
    return render(request, 'users/update.html', {'form': form})


@login_required(login_url='/login/')
def user_delete(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    messages.success(request, _('Учетная запись удалена'))
    return redirect('home')
