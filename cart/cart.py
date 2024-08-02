from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
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
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
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
        return len(self.cart)

    def get_total_price(self):
        return sum(Decimal(item['price']) * int(item['quantity'])
                   for item in self.cart.values())

    def total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_items(self):
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
