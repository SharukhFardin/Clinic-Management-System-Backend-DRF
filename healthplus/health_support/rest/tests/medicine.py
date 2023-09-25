from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from .payload import medicine_payload
from .urlhelpers import medicine_list_url


class MedicineRelatedTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.medicine_post = self.client.post(medicine_list_url, medicine_payload)

    def test_create_medicine(self):
        response = self.medicine_post
        self.assertEqual(self.respone.status_code, status.HTTP_201_CREATED)