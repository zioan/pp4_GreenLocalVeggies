from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal
from shop.models import Product
from .models import Order, OrderItem
from .forms import OrderCreateForm

User = get_user_model()


class OrderModelTest(TestCase):
    """Test suite for the Order model"""

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )

    def test_order_creation(self):
        """Test creating an order"""
        order = Order.objects.create(
            user=self.user,
            total_price=Decimal('100.00'),
            status='pending'
        )
        self.assertTrue(isinstance(order, Order))
        self.assertEqual(str(order), f'Order {order.pk}')

    def test_order_status_choices(self):
        """Test order status choices"""
        order = Order.objects.create(
            user=self.user,
            total_price=Decimal('100.00'),
            status='pending'
        )
        self.assertIn(order.status, dict(Order.STATUS_CHOICES))

    def test_order_cancel(self):
        """Test order cancellation"""
        order = Order.objects.create(
            user=self.user,
            total_price=Decimal('100.00'),
            status='pending'
        )
        self.assertTrue(order.cancel())
        self.assertEqual(order.status, 'cancelled')
        self.assertIsNotNone(order.cancelled_at)


class OrderItemModelTest(TestCase):
    """Test suite for the OrderItem model"""

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123'
        )
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('10.00'),
            stock=10,
            slug='test-product'
        )
        self.order = Order.objects.create(
            user=self.user,
            total_price=Decimal('100.00')
        )

    def test_order_item_creation(self):
        """Test creating an order item"""
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            price=Decimal('10.00'),
            quantity=2
        )
        self.assertTrue(isinstance(order_item, OrderItem))
        self.assertEqual(str(order_item), str(order_item.pk))


class OrderCreateFormTest(TestCase):
    """Test suite for the OrderCreateForm"""

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123'
        )

    def test_form_fields(self):
        """Test form fields"""
        form = OrderCreateForm(user=self.user)
        self.assertIn('saved_instruction', form.fields)


class OrderViewsTest(TestCase):
    """Test suite for order views"""

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.client = Client()
        self.client.login(email='testuser@example.com', password='testpass123')
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('10.00'),
            stock=10,
            slug='test-product'
        )

    def test_checkout_view(self):
        """Test the checkout view"""
        response = self.client.get(reverse('checkout'))
        self.assertIn(response.status_code, [200, 302])

        if response.status_code == 302:
            self.assertIn(response.url, [reverse(
                'cart_detail'), reverse('login')])
        else:
            self.assertTemplateUsed(response, 'orders/checkout.html')

    def test_order_history_view(self):
        """Test the order history view"""
        Order.objects.create(user=self.user, total_price=Decimal('100.00'))
        response = self.client.get(reverse('order-history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order-history.html')

    def test_order_detail_view(self):
        """Test the order detail view"""
        order = Order.objects.create(
            user=self.user,
            total_price=Decimal('100.00')
        )
        response = self.client.get(reverse('order-detail', args=[order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order-detail.html')

    def test_cancel_order_view(self):
        """Test the cancel order view"""
        order = Order.objects.create(
            user=self.user,
            total_price=Decimal('100.00'),
            status='pending'
        )
        response = self.client.post(reverse('cancel-order', args=[order.pk]))
        self.assertRedirects(response, reverse(
            'order-detail', args=[order.pk]))
        order.refresh_from_db()
        self.assertEqual(order.status, 'cancelled')
