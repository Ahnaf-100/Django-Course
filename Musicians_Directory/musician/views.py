from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def edit_musician(request, id):
   musician = models.Musician.objects.get(pk=id)
   musician_form = forms.MusicianForm(instance=musician)
   if request.method == 'POST':
      musician_form = forms.MusicianForm(request.POST,instance=musician)
      if musician_form.is_valid():
         musician_form.save()
         return redirect('homepage')
      else :
         musician_form = forms.AlbumForm()
   return render(request, 'add_album.html', {'form' : musician_form})