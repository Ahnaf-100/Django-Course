from django.shortcuts import render, redirect
from . forms import TaskCategoryForm
# Create your views here.

def add_category(request):
    form = TaskCategoryForm(request.POST)
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskCategoryForm()
    
    return render(request, 'add_category.html', {'form': form})
    
