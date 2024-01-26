from django.urls import path, include
from . import views

urlpatterns = [
    path('edit_musician/<int:id>', views.edit_musician, name='edit_musician'),

]