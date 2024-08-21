from django.test import TestCase, Client
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()


class CourierViewsTestCase(TestCase):
    """
    Test case for courier-related views.
    """

    def setUp(self):
        """
        Set up test data for the test case.

        This includes creating a courier user, a customer user,
        and an order associated with the customer.
        """
        self.courier = User.objects.create_user(
            email='courier@example.com',
            password='testpassword',
            is_courier=True,
            first_name='Courier',
            last_name='Test',
            street='Courier Street',
            house_number='1',
            city='Westerstede',
            zip_code='26655',
            phone_number='1234567890'
        )

        self.customer = User.objects.create_user(
            email='customer@example.com',
            password='testpassword',
            first_name='Customer',
            last_name='Test',
            street='Customer Street',
            house_number='2',
            city='Westerstede',
            zip_code='26655',
            phone_number='9876543210'
        )

        self.order = Order.objects.create(
            user=self.customer,
            total_price=100.00,
            status='shipped'
        )

        self.client = Client()

    def test_courier_dashboard_view(self):
        """
        Test that the courier dashboard view is accessible to couriers
        and displays the correct context.
        """
        self.client.login(
            email='courier@example.com',
            password='testpassword'
        )
        response = self.client.get(reverse('courier_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courier/dashboard.html')
        self.assertIn('shipped_orders', response.context)
        self.assertIn('delivered_orders', response.context)

    def test_order_detail_view(self):
        """
        Test that the order detail view is accessible to the courier
        assigned to the order.
        """
        self.client.login(username='courier@example.com',
                          password='testpassword')
        response = self.client.get(
            reverse('courier_order_detail', args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courier/order-detail.html')
        self.assertEqual(response.context['order'], self.order)

    def test_mark_delivered_view(self):
        """
        Test that a courier can mark an order as delivered,
        updating the order's status and delivery time.
        """
        self.client.login(username='courier@example.com',
                          password='testpassword')
        response = self.client.post(
            reverse('courier_mark_delivered', args=[self.order.pk]))
        self.assertRedirects(response, reverse('courier_dashboard'))
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'delivered')
        self.assertEqual(self.order.courier, self.courier)
        self.assertIsNotNone(self.order.delivered_at)

    def test_non_courier_access(self):
        """
        Test that a non-courier user (e.g., a customer) cannot access
        courier-specific views.

        This test checks for a redirection to the login page.
        """
        self.client.login(username='customer@example.com',
                          password='testpassword')
        response = self.client.get(reverse('courier_dashboard'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('courier_dashboard'))
        if isinstance(response, HttpResponseRedirect):
            self.assertIn('login', response.url)
        else:
            self.fail("Expected a redirect, but got a different response.")
