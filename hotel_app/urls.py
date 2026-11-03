from django.urls import path
from hotel_app import views

urlpatterns = [
    path('hotel/', views.HotelView.as_view()),
    path('room/', views.RoomView.as_view()),
    path('customer/', views.CustomerView.as_view()),
    path('services/', views.ServicesView.as_view()),
]