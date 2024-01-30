from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm

@login_required
def create_reservation(request):
    # Add your view logic here
    pass

@login_required
def list_reservations(request):
    # Add your view logic here
    pass

@login_required
def cancel_reservation(request, reservation_id):
    # Add your view logic here
    pass
