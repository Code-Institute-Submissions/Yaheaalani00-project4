from django.shortcuts import render, redirect
from .models import Reservation

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def create_reservation(request):
    if request.method == 'POST':
        # Process form data and create a new reservation
        reservation = Reservation(
            guest_name=request.POST['guest_name'],
            reservation_date=request.POST['reservation_date'],
            reservation_time=request.POST['reservation_time'],
            num_guests=request.POST['num_guests']
        )
        reservation.save()
        return redirect('reservation_list')
    return render(request, 'create_reservation.html')
