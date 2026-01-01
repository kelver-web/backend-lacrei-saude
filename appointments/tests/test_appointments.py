from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from professionals.models import Professional
from django.utils import timezone
from datetime import timedelta


class AppointmentAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='123456'
        )
        token = self.client.post('/api/token/', {
            'username': 'test',
            'password': '123456'
        }).data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.professional = Professional.objects.create(
            social_name='Alex',
            profession='Psicólogo',
            address='Rua X',
            contact='alex@email.com'
        )

    def test_create_appointment(self):
        payload = {
            'date': (timezone.now() + timedelta(days=1)).isoformat(),
            'professional': self.professional.id
        }

        response = self.client.post('/api/appointments/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_appointment_invalid_date(self):
        payload = {
            'date': (timezone.now() - timedelta(days=1)).isoformat(),
            'professional': self.professional.id
        }

        response = self.client.post('/api/appointments/', payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_list_appointments(self):
        response = self.client.get('/api/appointments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        self.client.credentials()
        response = self.client.get('/api/appointments/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_by_professional_not_found(self):
        response = self.client.get(
            '/api/appointments/by-professional/999/'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
