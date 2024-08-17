from django.test import TestCase, RequestFactory, Client
from django.http import HttpResponse
from django.urls import reverse
from unittest.mock import patch
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from decimal import Decimal
from shop.models import Product
from .cart import Cart


class CartTestCase(TestCase):
    """Test case for the Cart functionality"""

    def setUp(self):
        """Set up test data"""
        self.factory = RequestFactory()
        self.client = Client()

        # Create a simple image file for testing
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',  # empty file
            content_type='image/jpeg'
        )

        # Use the patch as a context manager to mock Cloudinary upload
        with patch('cloudinary.uploader.upload') as mock_upload:
            mock_upload.return_value = {
                'public_id': 'test_public_id',
                'secure_url': 'http://test.com/image.jpg'
            }

            # Create test products
            self.product = Product.objects.create(
                name="Test Product",
                price=Decimal("10.00"),
                stock=10,
                unit="kg",
                category="Vegetable",
                slug="test-product",
                image=self.image
            )
            self.product_out_of_stock = Product.objects.create(
                name="Out of Stock Product",
                price=Decimal("5.00"),
                stock=0,
                unit="kg",
                category="Vegetable",
                slug="out-of-stock-product",
                image=self.image
            )

    def _get_request_with_session(self):
        """Helper method to get a request object with a session"""
        request = self.factory.get('/')
        middleware = SessionMiddleware(get_response=lambda r: HttpResponse())
        middleware.process_request(request)
        request.session.save()
        return request

    def test_add_product_to_cart(self):
        """Test adding a product to the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=2)

        self.assertEqual(len(cart), 1)
        self.assertEqual(cart.cart[str(self.product.pk)]['quantity'], 2)

    def test_add_product_exceeding_stock(self):
        """Test adding a product with quantity exceeding stock"""
        request = self._get_request_with_session()
        cart = Cart(request)

        with self.assertRaises(ValidationError):
            cart.add(self.product, quantity=11)

    def test_add_out_of_stock_product(self):
        """Test adding an out of stock product"""
        request = self._get_request_with_session()
        cart = Cart(request)

        with self.assertRaises(ValidationError):
            cart.add(self.product_out_of_stock, quantity=1)

    def test_update_product_quantity(self):
        """Test updating the quantity of a product in the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=2)
        cart.add(self.product, quantity=3, update_quantity=True)

        self.assertEqual(cart.cart[str(self.product.pk)]['quantity'], 3)

    def test_remove_product_from_cart(self):
        """Test removing a product from the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=2)
        cart.remove(self.product)

        self.assertEqual(len(cart), 0)

    def test_get_total_price(self):
        """Test calculating the total price of the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=2)

        expected_total = Decimal("20.00")
        self.assertEqual(cart.get_total_price(), expected_total)

    def test_clear_cart(self):
        """Test clearing all items from the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=2)
        cart.clear()

        self.assertEqual(len(cart), 0)

    def test_get_item_quantity(self):
        """Test getting the quantity of a specific item in the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=3)

        self.assertEqual(cart.get_item_quantity(self.product.pk), 3)

    def test_get_items(self):
        """Test getting all items in the cart"""
        request = self._get_request_with_session()
        cart = Cart(request)
        cart.add(self.product, quantity=2)

        items = cart.get_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['product'], self.product)
        self.assertEqual(items[0]['quantity'], 2)
        self.assertEqual(items[0]['price'], Decimal("10.00"))
        self.assertEqual(items[0]['total_price'], Decimal("20.00"))

    @patch('cloudinary.uploader.upload')
    def test_add_to_cart_view(self, mock_upload):
        """Test the add_to_cart view"""
        mock_upload.return_value = {'secure_url': 'http://test.com/image.jpg'}
        url = reverse('add_to_cart', args=[self.product.pk])
        response = self.client.post(url, {'quantity': 2})

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {
            'status': 'success',
            'message': '2 kg of Test Product added to cart.',
            'cart_count': 1,
            'product_in_cart': True
        })

    @patch('cloudinary.uploader.upload')
    def test_add_to_cart_view_invalid_quantity(self, mock_upload):
        """Test the add_to_cart view with invalid quantity"""
        mock_upload.return_value = {'secure_url': 'http://test.com/image.jpg'}
        url = reverse('add_to_cart', args=[self.product.pk])
        response = self.client.post(url, {'quantity': -1})

        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertEqual(response_data['status'], 'error')
        self.assertIn('Invalid quantity', response_data['message'])

    @patch('cloudinary.uploader.upload')
    def test_update_cart_view(self, mock_upload):
        """Test the update_cart view"""
        mock_upload.return_value = {'secure_url': 'http://test.com/image.jpg'}
        # First, add an item to the cart
        self.client.post(reverse('add_to_cart', args=[
                         self.product.pk]), {'quantity': 1})

        # Then, update its quantity
        url = reverse('update_cart', args=[self.product.pk])
        response = self.client.post(url, {'quantity': 3})

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {
            'status': 'success',
            'cart_total': '30.00',
            'cart_count': 3,
        })

    @patch('cloudinary.uploader.upload')
    def test_remove_from_cart_view(self, mock_upload):
        """Test the remove_from_cart view"""
        mock_upload.return_value = {'secure_url': 'http://test.com/image.jpg'}
        # First, add an item to the cart
        self.client.post(reverse('add_to_cart', args=[
                         self.product.pk]), {'quantity': 1})

        # Then, remove it
        url = reverse('remove_from_cart', args=[self.product.pk])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, reverse('cart_detail'))

    @patch('cloudinary.uploader.upload')
    def test_cart_detail_view(self, mock_upload):
        """Test the cart_detail view"""
        mock_upload.return_value = {'secure_url': 'http://test.com/image.jpg'}
        # Add an item to the cart
        self.client.post(reverse('add_to_cart', args=[
                         self.product.pk]), {'quantity': 2})

        url = reverse('cart_detail')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your shopping cart')
        self.assertContains(response, 'Test Product')
        self.assertContains(response, '20.00')  # Total price for 2 items

    def test_cart_detail_view_empty_cart(self):
        """Test the cart_detail view with an empty cart"""
        url = reverse('cart_detail')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your cart is empty.')
        self.assertContains(response, 'Go to shop')
