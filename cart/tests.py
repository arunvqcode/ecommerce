from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ProductDetails, Cart, CartItem

class CartAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = ProductDetails.objects.create(
            name='Test Product',
            price=10.0,
            description='Test description',
            image='test_image.jpg'
        )
        
    

    def test_add_to_cart(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'product_id': self.product.id,
            'quantity': 2
        }
        response = self.client.post('add-to-cart', data,)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # You should access the product name from the response data
        self.assertEqual(response.data.get('product_name'), self.product.name)
        self.assertEqual(response.data.get('quantity'), 2)

    def test_list_cart_items(self):
        self.client.force_authenticate(user=self.user)
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=3)
        response = self.client.get('view-cart-list')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product']['name'], self.product.name)
        self.assertEqual(response.data[0]['quantity'], 3)
