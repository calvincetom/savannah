"""Module for unit tests of serializers."""
from django.contrib.auth.models import User  # Import User model if needed for OrderSerializer
from django.test import TestCase
from rest_framework.test import APITestCase
from .serializers import CustomerSerializer, OrderSerializer
from .models import Customer  # Import Customer model

class CustomerSerializerTestCase(TestCase):
    """Test suite for the CustomerSerializer class."""

    def setUp(self):
        """Set up test data."""
        self.valid_data = {
            'name': 'John Doe',
            'phone_number': '+254743787076',
            'code': 'JD001'
        }

    def test_valid_serializer(self):
        """Test that the serializer is valid with proper data."""
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_field_content(self):
        """Test if serializer fields contain correct data."""
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        for field in ['name', 'phone_number', 'code']:
            self.assertEqual(serializer.validated_data[field], self.valid_data[field])

    def test_serializer_with_invalid_data(self):
        """Test serializer with invalid data."""
        invalid_data = self.valid_data.copy()
        invalid_data['name'] = ''  # Empty name should be invalid
        serializer = CustomerSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_contains_expected_fields(self):
        """Test if serializer contains all expected fields."""
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        expected_fields = set(['name', 'phone_number', 'code'])
        self.assertEqual(set(serializer.validated_data.keys()), expected_fields)
        # Note: 'id' field might not be in validated_data, so we check for it separately
        self.assertIn('id', serializer.fields)


class OrderSerializerTests(APITestCase):
    """Test suite for the OrderSerializer class."""

    def setUp(self):
        """Set up valid data for testing the serializer."""
        # Create a test user and customer
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(name='Test Customer', phone_number='+254743787076', code='TC001')
        
        self.valid_data = {
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': 10.00,
            'time': '2024-01-01T12:00:00Z'
        }

    def test_valid_serializer(self):
        """Test that the serializer is valid with proper data."""
        serializer = OrderSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['amount'], 10.00)

    def test_negative_amount_validation(self):
        """Test that a negative amount raises a validation error."""
        invalid_data = self.valid_data.copy()
        invalid_data['amount'] = -5.00

        serializer = OrderSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('amount', serializer.errors)
        self.assertEqual(
            serializer.errors['amount'][0],
            'Amount entered cannot be negative.'
        )

    def test_zero_amount_validation(self):
        """Test that an amount of zero is accepted as valid."""
        valid_data_with_zero = self.valid_data.copy()
        valid_data_with_zero['amount'] = 0.00

        serializer = OrderSerializer(data=valid_data_with_zero)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['amount'], 0.00)