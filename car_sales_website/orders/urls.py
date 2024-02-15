from django.urls import path
from . import views

urlpatterns = [
    path('order_history/', views.OrderHistoryView.as_view(), name='order_history'),
    path('place_order/<int:car_id>', views.place_order, name='place_order'),
    # Add other order-related URLs as needed
]
