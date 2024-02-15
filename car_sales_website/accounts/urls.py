from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    # path('profile/', views.profile, name="profile"),
    path('profile/pass_change/', views.pass_change, name="pass_change"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('profile/edit/', views.edit_profile, name="edit_profile"),
]
