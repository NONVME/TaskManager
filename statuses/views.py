from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import StatusesForm
from .models import Statuses


@login_required(login_url='/login/')
def get_statuses(request):
    statuses = Statuses.objects.order_by('-pk')
    return render(request, 'statuses/statuses.html', {
        'title': _('Статусы'),
        'statuses': statuses
    })


@login_required(login_url='/login/')
def status_create(request):
    if request.method == 'POST':
        form = StatusesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Статус успешно создан'))
            return redirect('statuses')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = StatusesForm()
    return render(request, 'statuses/statuses_create.html', {'form': form})


@login_required(login_url='/login/')
def status_change(request, pk):
    status = Statuses.objects.get(pk=pk)
    if request.method == 'POST':
        form = StatusesForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, _('Статус изменён'))
            return redirect('statuses')
        else:
            messages.error(request, _('Форма заполнена некорректно'))

    form = StatusesForm(instance=status)
    return render(request, 'statuses/status_update.html', {'form': form})


@login_required(login_url='/login/')
def status_delete(request, pk):
    status = Statuses.objects.get(pk=pk)
    status.delete()
    messages.success(request, _('Статуc удалён'))
    return redirect('statuses')
