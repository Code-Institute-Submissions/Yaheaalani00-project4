from django.db import models

class Reservation(models.Model):
    guest_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    num_guests = models.IntegerField()

    def __str__(self):
        return f"{self.guest_name} - {self.reservation_date} - {self.reservation_time}"
    
    class Meta:
        app_label = 'reservations'
