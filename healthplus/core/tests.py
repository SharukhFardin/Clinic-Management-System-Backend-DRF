from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status


""" Placeholder code for now. """


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "user@example.com", "new1234password"
        )

        self.client.force_authenticate(self.auth_user)

    def tearDown(self):
        self.client.logout()
