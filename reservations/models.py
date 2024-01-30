from django.db import models


class Reservation(models.Model):
    # your model fields here

    class Meta:
        app_label = 'reservations'
