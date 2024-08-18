from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from decimal import Decimal
from shop.models import Product


class ShopViewsTest(TestCase):
    """
    Test case for shop views functionality.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.
        Creates a test client, a mock image, and a test product.
        """
        self.client = Client()

        # Create a simple image file for testing
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',  # empty file
            content_type='image/jpeg'
        )

        # Use the patch as a context manager to mock Cloudinary upload
        patcher = patch('cloudinary.uploader.upload')
        self.mock_upload = patcher.start()
        self.mock_upload.return_value = {
            'public_id': 'test_public_id',
            'secure_url': 'http://test.com/image.jpg'
        }
        self.addCleanup(patcher.stop)

        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=Decimal('9.99'),
            stock=100,
            unit="kg",
            category="Vegetable",
            slug="test-product",
            image=self.image
        )

    def test_index_view(self):
        """
        Test the index view to ensure it returns a 200 status code,
        uses the correct template, and contains the test product.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/index.html')
        self.assertContains(response, "Test Product")

    def test_product_details_view(self):
        """
        Test the product details view to ensure it returns a 200 status code,
        uses the correct template, and contains the test product details.
        """
        response = self.client.get(
            reverse('product-details', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product-details.html')
        self.assertContains(response, "Test Product")

    def test_add_to_cart(self):
        """
        Test the add to cart functionality to ensure it returns a 200 status
        code and the correct JSON response when adding a product to the cart.
        """
        response = self.client.post(
            reverse('add_to_cart', args=[self.product.pk]), {'quantity': 1})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {
            'status': 'success',
            'message': '1 kg of Test Product added to cart.',
            'cart_count': 1,
            'product_in_cart': True
        })

    def test_about_view(self):
        """
        Test the about view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/about.html')

    def test_contact_view(self):
        """
        Test the contact view to ensure it returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/contact.html')


class ProductSearchTest(TestCase):
    """
    Test case for product search functionality.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.
        Creates a test client, a mock image, and two test products.
        """
        self.client = Client()
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        patcher = patch('cloudinary.uploader.upload')
        self.mock_upload = patcher.start()
        self.mock_upload.return_value = {
            'public_id': 'test_public_id',
            'secure_url': 'http://test.com/image.jpg'
        }
        self.addCleanup(patcher.stop)

        Product.objects.create(
            name="Apple",
            description="Fresh red apple",
            price=Decimal('1.99'),
            stock=100,
            unit="kg",
            category="Fruit",
            slug="apple",
            image=self.image
        )
        Product.objects.create(
            name="Banana",
            description="Yellow banana",
            price=Decimal('0.99'),
            stock=150,
            unit="kg",
            category="Fruit",
            slug="banana",
            image=self.image
        )

    def test_search_results(self):
        """
        Test the search functionality to ensure it returns the correct results.
        """
        response = self.client.get(reverse('index'), {'q': 'apple'})
        self.assertContains(response, "Apple")
        self.assertNotContains(response, "Banana")

    def test_empty_search(self):
        """
        Test the search functionality with an empty query to ensure it returns
        all products.
        """
        response = self.client.get(reverse('index'), {'q': ''})
        self.assertContains(response, "Apple")
        self.assertContains(response, "Banana")


class ProductFilterTest(TestCase):
    """
    Test case for product filtering functionality.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.
        Creates a test client, a mock image, and two test products.
        """
        self.client = Client()
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        patcher = patch('cloudinary.uploader.upload')
        self.mock_upload = patcher.start()
        self.mock_upload.return_value = {
            'public_id': 'test_public_id',
            'secure_url': 'http://test.com/image.jpg'
        }
        self.addCleanup(patcher.stop)

        Product.objects.create(
            name="Apple",
            description="Fresh red apple",
            price=Decimal('1.99'),
            stock=100,
            unit="kg",
            category="Fruit",
            slug="apple",
            image=self.image
        )
        Product.objects.create(
            name="Carrot",
            description="Orange carrot",
            price=Decimal('0.99'),
            stock=150,
            unit="kg",
            category="Vegetable",
            slug="carrot",
            image=self.image
        )

    def test_category_filter(self):
        """
        Test the category filter functionality to ensure it returns
        the correct results.
        """
        response = self.client.get(reverse('index'), {'category': 'Fruit'})
        self.assertContains(response, "Apple")
        self.assertNotContains(response, "Carrot")

    def test_price_sorting(self):
        """
        Test the price sorting functionality to ensure products
        are sorted correctly.
        """
        response = self.client.get(reverse('index'), {'sort': 'price_asc'})
        content = response.content.decode('utf-8')
        self.assertTrue(content.index("Carrot") < content.index("Apple"))

    def test_availability_filter(self):
        """
        Test the availability filter functionality to ensure it returns
        only in-stock items.
        """
        Product.objects.create(
            name="Out of Stock Item",
            description="This item is out of stock",
            price=Decimal('5.99'),
            stock=0,
            unit="piece",
            category="Vegetable",
            slug="out-of-stock",
            image=self.image
        )
        response = self.client.get(
            reverse('index'), {'availability': 'in_stock'})
        self.assertContains(response, "Apple")
        self.assertContains(response, "Carrot")
        self.assertNotContains(response, "Out of Stock Item")
