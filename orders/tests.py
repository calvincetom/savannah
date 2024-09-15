from rest_framework.test import APITestCase
from .models import Customer, Order

class CustomerOrderTest(APITestCase):
    def test_create_customer(self):
        data = {'name', 'John Doe', 'code', 'JD001'}
        response = self.client.post('api/v1/customers/', data)
        self.assertEqual(response.status_code, 201)