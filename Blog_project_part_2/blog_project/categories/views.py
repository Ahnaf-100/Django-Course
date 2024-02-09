from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_category(request):
    category_form = forms.CategoryForm(request.POST)
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
        else:
            author_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_form})
 