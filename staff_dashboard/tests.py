from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order
from shop.models import Product

User = get_user_model()


class StaffDashboardTestCase(TestCase):
    """
    Test case for the Staff Dashboard functionality.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.
        """
        # Create a staff user
        self.staff_user = User.objects.create_user(
            email='staff@example.com',
            password='testpassword',
            is_staff=True
        )

        # Create a non-staff user
        self.regular_user = User.objects.create_user(
            email='user@example.com',
            password='testpassword'
        )

        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            stock=100,
            unit='kg',
            category='Vegetable',
            slug='test-product'
        )

        # Create a test order
        self.order = Order.objects.create(
            user=self.regular_user,
            total_price=10.00,
            status='pending'
        )

        self.client = Client()

    def test_staff_dashboard_access(self):
        """
        Test that staff users can access the dashboard and
        non-staff users cannot.
        """
        # Staff user should be able to access the dashboard
        self.client.login(email='staff@example.com', password='testpassword')
        response = self.client.get(reverse('staff_dashboard:order_list'))
        self.assertEqual(response.status_code, 200)

        # Non-staff user should be redirected
        self.client.login(email='user@example.com', password='testpassword')
        response = self.client.get(reverse('staff_dashboard:order_list'))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_order_list_view(self):
        """
        Test the order list view in the staff dashboard.
        """
        self.client.login(email='staff@example.com', password='testpassword')
        response = self.client.get(reverse('staff_dashboard:order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff_dashboard/order-list.html')
        self.assertContains(response, self.order.pk)

    def test_order_detail_view(self):
        """
        Test the order detail view in the staff dashboard.
        """
        self.client.login(email='staff@example.com', password='testpassword')
        response = self.client.get(
            reverse('staff_dashboard:order_detail', args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff_dashboard/order-detail.html')
        self.assertContains(response, self.order.user.email)

    def test_update_order_status(self):
        """
        Test updating the order status through the staff dashboard.
        """
        self.client.login(email='staff@example.com', password='testpassword')
        response = self.client.post(
            reverse('staff_dashboard:update_order_status',
                    args=[self.order.pk]),
            {'status': 'processing'}
        )
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Refresh the order from the database
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'processing')

    def test_filter_orders(self):
        """
        Test filtering orders by status in the staff dashboard.
        """
        Order.objects.create(user=self.regular_user,
                             total_price=20.00, status='processing')

        self.client.login(email='staff@example.com', password='testpassword')
        response = self.client.get(
            reverse('staff_dashboard:order_list') + '?status=pending')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['orders']), 1)
        self.assertEqual(response.context['orders'][0].status, 'pending')

    def test_assign_courier(self):
        """
        Test assigning a courier to an order.
        """
        courier = User.objects.create_user(
            email='courier@example.com',
            password='testpassword',
            is_courier=True
        )

        self.client.login(email='staff@example.com', password='testpassword')
        url = reverse('staff_dashboard:update_order_status',
                      args=[self.order.pk])
        data = {
            'status': 'shipped',
            'courier': courier.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Refresh the order from the database
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'shipped')
        self.assertEqual(self.order.courier, courier)
