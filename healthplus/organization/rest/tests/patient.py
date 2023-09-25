from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class PatientRegistrationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        user_payload = {
            "name": "Sharukh Fardin",
            "password": "12345",
            "email": "sharukh@gmail.com",
        }
        self.user = self.client.post("/me/patient/register", user_payload)

        self.org_payload = {"user": self.user, "name": "name"}

        self.org = self.client.post("api_url", self.org_payload)

    def test_create_organization(self):
        response = self.org
        self.assertEqual(response.org.data["name"], response.org_payload()["name"])
        self.assertEqual(response.org.data['email'], response.org_payload()['email'])
