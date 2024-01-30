from django.urls import path
from reservations import views

urlpatterns = [
    # Add paths to reservations app views
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/create/', views.create_reservation, name='create_reservation'),
    # Other URL patterns...
]
