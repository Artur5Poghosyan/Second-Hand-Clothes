from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class GarmentAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            full_name='Test User',
            address='100 Test Street'
        )

        # Generate a token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Set the Authorization header with the access token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Add garments or other required data here.

    def test_garment_list(self):
        # Send a GET request to the GarmentListView endpoint
        response = self.client.get('/api/clothes/')

        # Assert that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
