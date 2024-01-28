from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskModelForm
# Create your views here.
# task/views.py


def add_task(request):
    form = TaskModelForm(request.POST)
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskModelForm()
    
    return render(request, 'add_task.html', {'form': form})

    


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskModelForm(instance=task)
    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
        
    return render(request, 'add_task.html',{'form' : task_form} )


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')