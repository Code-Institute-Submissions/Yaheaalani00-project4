from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Reservation

class ReservationViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.table = Table.objects.create(capacity=4)
        self.reservation = Reservation.objects.create(user=self.user, table=self.table, date='2024-01-31', time='18:00:00')

    def test_create_reservation_view(self):
        response = self.client.get(reverse('create_reservation'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('create_reservation'), {'table': self.table.id, 'date': '2024-02-01', 'time': '19:00:00'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 2)

    def test_list_reservations_view(self):
        response = self.client.get(reverse('reservation_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.reservation.date)

    def test_cancel_reservation_view(self):
        response = self.client.post(reverse('cancel_reservation', args=(self.reservation.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 0)
