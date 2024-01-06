
from django.urls import path
from . import views

urlpatterns = [
    path('food_items/', views.show_items,name='food_items'),

]
