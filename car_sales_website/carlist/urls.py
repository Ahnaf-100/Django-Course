from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('brand/<slug:brand_slug>/', views.home, name='brand_wise_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
   
]
