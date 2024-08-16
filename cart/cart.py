from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    """
    A class to represent the shopping cart.
    """

    def __init__(self, request):
        """
        Initialize the cart.

        Args:
            request: The current request object.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Create a new cart if one doesn't exist
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.

        Args:
            product: The product to add or update.
            quantity (int): The quantity to add or set.
            update_quantity (bool): If True, set the quantity instead of
                adding to it.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            self.cart[product_id]['quantity'] = int(
                self.cart[product_id]['quantity']) + int(quantity)

        self.save()

    def save(self):
        """Mark the session as modified to make sure it gets saved."""
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.

        Args:
            product: The product to remove.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the
        database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.pk)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['quantity'])
            yield item

    def __len__(self):
        """Return the total number of items in the cart."""
        return len(self.cart)

    def get_total_price(self):
        """Calculate the total price of all items in the cart."""
        return sum(Decimal(item['price']) * int(item['quantity'])
                   for item in self.cart.values())

    def total_quantity(self):
        """Calculate the total quantity of all items in the cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_item_quantity(self, product_id):
        """
        Get the quantity of a specific product in the cart.

        Args:
            product_id: The ID of the product.

        Returns:
            int: The quantity of the product in the cart.
        """
        return self.cart.get(str(product_id), {}).get('quantity', 0)

    def clear(self):
        """Remove the cart from session."""
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_items(self):
        """
        Get all items in the cart with their associated product information.

        Returns:
            list: A list of dictionaries containing product and
                cart information.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart_items = []
        for product in products:
            item = self.cart[str(product.pk)]
            cart_items.append({
                'product': product,
                'quantity': int(item['quantity']),
                'price': Decimal(item['price']),
                'total_price': Decimal(item['price']) * int(item['quantity'])
            })

        return cart_items
