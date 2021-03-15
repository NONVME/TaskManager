from django.shortcuts import render

from .models import User


def users(request):
    users = User.objects.order_by('-id')
    return render(request, 'users/users.html', {'title': 'Список пользователей', 'users': users})


def create(request):
    pass


def update(request, pk):
    pass


def delete(request, pk):
    pass
