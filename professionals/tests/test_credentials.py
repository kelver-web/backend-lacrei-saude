from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from professionals.models import Professional


class ProfessionalAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        response = self.client.post(
            '/api/token/',
            {
                'username': 'testuser',
                'password': 'testpassword'
            }
        )

        self.token = response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )

        self.payload = {
            'social_name': 'Test Professional',
            'profession': 'Test Profession',
            'address': 'Test Address',
            'contact': 'Test Contact'
        }

    def test_create_professional(self):
        response = self.client.post(
            '/api/professionals/',
            self.payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_professionals(self):
        response = self.client.get('/api/professionals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
