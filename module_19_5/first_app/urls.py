from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.home),
    path('signup/', views.signup, name="signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('profile/', views.profile, name="profile"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('pass_change1/', views.pass_change1, name="pass_change1"),
    path('pass_change2/', views.pass_change2, name="pass_change2"),

]