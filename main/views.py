from django.shortcuts import render, redirect
# from .forms import taskform


def index(request):
    return render(request, 'main/index.html')


# def tasks(request):
    # error = ''
    # if request.method == 'POST':
        # form = TaskForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return redirect('home')
        # else:
            # error = 'Форма заполненна некорректно'

    # form = TaskForm()
    # context = {
        # 'form': form,
        # 'error': error,
    # }
    # return render(request, 'main/tasks.html', context)
