from django.db import models


class Reservation(models.Model):
    # Your model fields here

    class Meta:
        app_label = 'reservations'
