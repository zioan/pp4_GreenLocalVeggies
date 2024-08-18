from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import DeliveryInstruction
from .forms import DeliveryInstructionForm

User = get_user_model()


class DeliveryInstructionModelTest(TestCase):
    """
    Test case for the DeliveryInstruction model.
    """

    def setUp(self):
        """
        Set up test data for the DeliveryInstruction model tests.
        """
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.instruction = DeliveryInstruction.objects.create(
            user=self.user,
            title='Test Instruction',
            instruction='Leave at the door'
        )

    def test_delivery_instruction_creation(self):
        """
        Test that a DeliveryInstruction instance can be created with
        correct attributes.
        """
        self.assertEqual(self.instruction.user, self.user)
        self.assertEqual(self.instruction.title, 'Test Instruction')
        self.assertEqual(self.instruction.instruction, 'Leave at the door')

    def test_delivery_instruction_str_representation(self):
        """
        Test the string representation of a DeliveryInstruction instance.
        """
        expected_str = "Test Instruction - testuser@example.com"
        self.assertEqual(str(self.instruction), expected_str)


class DeliveryInstructionFormTest(TestCase):
    """
    Test case for the DeliveryInstructionForm.
    """

    def test_delivery_instruction_form_valid_data(self):
        """
        Test that the DeliveryInstructionForm is valid with correct data.
        """
        form_data = {
            'title': 'Test Instruction',
            'instruction': 'Leave at the front door'
        }
        form = DeliveryInstructionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_delivery_instruction_form_invalid_data(self):
        """
        Test that the DeliveryInstructionForm is invalid with incorrect data.
        """
        form_data = {
            'title': '',  # Title is required
            'instruction': 'Leave at the front door'
        }
        form = DeliveryInstructionForm(data=form_data)
        self.assertFalse(form.is_valid())


class DeliveryInstructionViewsTest(TestCase):
    """
    Test case for the DeliveryInstruction views.
    """

    def setUp(self):
        """
        Set up test data and client for the DeliveryInstruction views tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.instruction = DeliveryInstruction.objects.create(
            user=self.user,
            title='Test Instruction',
            instruction='Leave at the door'
        )
        self.client.login(email='testuser@example.com', password='testpass123')

    def test_instruction_create_view(self):
        """
        Test the instruction_create view for creating
        a new DeliveryInstruction.
        """
        url = reverse('instruction_create')
        data = {
            'title': 'New Instruction',
            'instruction': 'Ring the doorbell twice'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(DeliveryInstruction.objects.filter(
            title='New Instruction').exists())

    def test_instruction_update_view(self):
        """
        Test the instruction_update view for updating
        an existing DeliveryInstruction.
        """
        url = reverse('instruction_update', args=[self.instruction.pk])
        data = {
            'title': 'Updated Instruction',
            'instruction': 'Leave at the back door'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.instruction.refresh_from_db()
        self.assertEqual(self.instruction.title, 'Updated Instruction')
        self.assertEqual(self.instruction.instruction,
                         'Leave at the back door')

    def test_instruction_delete_view(self):
        """
        Test the instruction_delete view for deleting a DeliveryInstruction.
        """
        url = reverse('instruction_delete', args=[self.instruction.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(DeliveryInstruction.objects.filter(
            pk=self.instruction.pk).exists())

    def test_instruction_detail_view(self):
        """
        Test the instruction_detail view for retrieving a DeliveryInstruction.
        """
        url = reverse('instruction_detail', args=[self.instruction.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'Test Instruction')
        self.assertEqual(response.json()['instruction'], 'Leave at the door')
