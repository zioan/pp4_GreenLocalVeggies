from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Order
from django.conf import settings
from django.contrib import messages
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                # Stripe expects amount in cents
                amount=int(order.total_price * 100),
                currency='eur',
                metadata={'order_id': order.id}
            )
            return render(request, 'orders/checkout.html', {
                'client_secret': intent.client_secret,
                'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
                'order': order,
                'cart': cart,
                'form': form,
            })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'form': form,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
    })


def payment_success(request):
    payment_intent_id = request.GET.get('payment_intent')
    try:
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        order_id = intent.metadata.get('order_id')

        if not order_id:
            raise ValueError("No order ID found in payment intent metadata")

        order = get_object_or_404(Order, id=order_id)

        if intent.status == 'succeeded':
            order.paid = True
            order.status = 'processing'
            order.save()
            # Clear the cart
            cart = Cart(request)
            cart.clear()
            messages.success(request, f"Payment successful! Your order #{
                             order.pk} is now being processed.")
            return render(request, 'orders/payment_success.html', {
                "order": order
            })
        else:
            messages.error(request, "Payment was not successful.")
            return render(request, 'orders/payment_failed.html')

    except stripe.error.StripeError as e:  # type: ignore
        # Handle Stripe-specific errors
        messages.error(request, f"An error occurred: {str(e)}")
        return render(request, 'orders/payment_failed.html')

    except Exception as e:
        messages.error(
            request, f"An unexpected error occurred: {str(e)}.")
        return render(request, 'orders/payment_failed.html')


@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order-history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order-detail.html', {'order': order})
