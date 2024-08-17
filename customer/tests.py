from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import (
    CustomerRegistrationForm,
    CustomerLoginForm,
    CustomerProfileForm
)


class CustomerModelTest(TestCase):
    """
    Test case for the CustomerUser model.
    """

    def setUp(self):
        """
        Set up test data for CustomerUser model tests.
        """
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'first_name': 'John',
            'last_name': 'Doe',
            'street': 'Test Street',
            'house_number': '123',
            'city': 'Westerstede',
            'zip_code': '26655',
            'phone_number': '1234567890'
        }

    def test_create_user(self):
        """
        Test creating a regular user with the CustomerUser model.
        """
        user = get_user_model().objects.create_user(**self.user_data)
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Test creating a superuser with the CustomerUser model.
        """
        admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpassword123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class CustomerViewsTest(TestCase):
    """
    Test case for customer-related views.
    """

    def setUp(self):
        """
        Set up test data and client for view tests.
        """
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'confirm_password': 'testpassword123',
            'first_name': 'John',
            'last_name': 'Doe',
            'street': 'Test Street',
            'house_number': '123',
            'city': 'Westerstede',
            'zip_code': '26655',
            'phone_number': '1234567890'
        }

    def test_register_view_GET(self):
        """
        Test GET request to the register view.
        """
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/register.html')
        self.assertIsInstance(
            response.context['form'], CustomerRegistrationForm)

    def test_register_view_POST_valid(self):
        """
        Test POST request to the register view with valid data.
        """
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(get_user_model().objects.filter(
            email='test@example.com').exists())

    def test_register_view_POST_invalid(self):
        """
        Test POST request to the register view with invalid data.
        """
        invalid_data = self.user_data.copy()
        invalid_data['email'] = 'invalid-email'
        response = self.client.post(self.register_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)  # Stay on the same page
        self.assertFalse(get_user_model().objects.filter(
            email='invalid-email').exists())

    def test_login_view_GET(self):
        """
        Test GET request to the login view.
        """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/login.html')
        self.assertIsInstance(response.context['form'], CustomerLoginForm)

    def test_login_view_POST_valid(self):
        """
        Test POST request to the login view with valid credentials.
        """
        user_data = self.user_data.copy()
        # Remove confirm_password as it's not needed
        user_data.pop('confirm_password')
        get_user_model().objects.create_user(**user_data)

        response = self.client.post(self.login_url, {
            'username': 'test@example.com',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success

    def test_profile_view_authenticated(self):
        """
        Test access to profile view for authenticated users.
        """
        user_data = self.user_data.copy()
        # Remove confirm_password as it's not needed
        user_data.pop('confirm_password')
        get_user_model().objects.create_user(**user_data)

        self.client.login(username='test@example.com',
                          password='testpassword123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/profile.html')

    def test_profile_view_unauthenticated(self):
        """
        Test access to profile view for unauthenticated users.
        """
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)  # Redirect to login


class CustomerFormsTest(TestCase):
    """
    Test case for customer-related forms.
    """

    def test_customer_registration_form_valid(self):
        """
        Test CustomerRegistrationForm with valid data.
        """
        form_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'confirm_password': 'testpassword123',
            'first_name': 'John',
            'last_name': 'Doe',
            'street': 'Test Street',
            'house_number': '123',
            'city': 'Westerstede',
            'zip_code': '26655',
            'phone_number': '1234567890'
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_customer_registration_form_passwords_dont_match(self):
        """
        Test CustomerRegistrationForm with mismatched passwords.
        """
        form_data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'confirm_password': 'differentpassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'street': 'Test Street',
            'house_number': '123',
            'city': 'Westerstede',
            'zip_code': '26655',
            'phone_number': '1234567890'
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('confirm_password', form.errors)

    def test_customer_profile_form_valid(self):
        """
        Test CustomerProfileForm with valid data.
        """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'street': 'Test Street',
            'house_number': '123',
            'city': 'Westerstede',
            'zip_code': '26655',
            'email': 'test@example.com',
            'phone_number': '1234567890'
        }
        form = CustomerProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_customer_profile_form_invalid_email(self):
        """
        Test CustomerProfileForm with an invalid email address.
        """
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'street': 'Test Street',
            'house_number': '123',
            'city': 'Westerstede',
            'zip_code': '26655',
            'email': 'invalid-email',
            'phone_number': '1234567890'
        }
        form = CustomerProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
