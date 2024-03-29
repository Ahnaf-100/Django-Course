from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="user_login"),
    path('profile/', views.profile, name="profile"),
    path('profile/pass_change/', views.pass_change, name="pass_change"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('logout/', views.user_logout, name="user_logout"),
]