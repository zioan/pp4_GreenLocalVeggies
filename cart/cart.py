from decimal import Decimal
from django.conf import settings
from shop.models import Product
from math import ceil


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=Decimal('1'), update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': '0', 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = str(quantity)
        else:
            self.cart[product_id]['quantity'] = str(
                Decimal(self.cart[product_id]['quantity']) + quantity)

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.pk)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['quantity'] = Decimal(item['quantity'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return int(ceil(sum(Decimal(item['quantity'])
                            for item in self.cart.values())))

    def get_total_price(self):
        return sum(Decimal(item['price']) * Decimal(item['quantity'])
                   for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_items(self):
        return list(self.__iter__())
