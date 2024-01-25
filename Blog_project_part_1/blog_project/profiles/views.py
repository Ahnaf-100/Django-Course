from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_profile(request):
    profile_form = forms.ProfilerForm(request.POST)
    if request.method == 'POST':
        # author_form = forms.AuthorForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
        else:
            profile_form = forms.ProfilerForm()
    return render(request, 'add_profile.html', {'form' : profile_form})
 