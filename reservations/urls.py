from django.urls import path
from .views import create_reservation, list_reservations, cancel_reservation

urlpatterns = [
    path('create/', create_reservation, name='create_reservation'),
    path('list/', list_reservations, name='reservation_list'),
    path('cancel/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
]
