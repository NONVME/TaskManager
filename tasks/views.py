from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import TasksForm
from .models import Tasks


@login_required(login_url='/login/')
def get_tasks(request):
    tasks = Tasks.objects.order_by('-pk')
    return render(request, 'tasks/tasks.html', {
        'title': _('Задачи'),
        'tasks': tasks
    })


@login_required(login_url='/login/')
def task_create(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Задача успешно создана'))
            return redirect('tasks')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = TasksForm()
    return render(request, 'tasks/task_create.html', {'form': form})


@login_required(login_url='/login/')
def task_change(request, pk):
    tasks = Tasks.objects.get(pk=pk)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            messages.success(request, _('Задача изменёна'))
            return redirect('tasks')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = TasksForm(instance=tasks)
    return render(request, 'tasks/task_update.html', {'form': form})


@login_required(login_url='/login/')
def task_delete(request, pk):
    tasks = Tasks.objects.get(pk=pk)
    tasks.delete()
    messages.success(request, _('Задача удалена'))
    return redirect('tasks')
