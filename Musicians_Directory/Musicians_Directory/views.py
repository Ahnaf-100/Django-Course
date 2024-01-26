from django.shortcuts import render
from album.models import Album

def home(requset):
    data= Album.objects.all
    return render(requset, 'home.html', {'data' : data})