from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
from django.contrib import messages
import stripe

# Set up Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """
    Handles the checkout process, including displaying the order form,
    checking stock availability, creating a Stripe PaymentIntent if the form
    is valid, and reducing stock after successful order creation.
    """
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, "Please add items before checking out.")
        return redirect('cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST, user=request.user)
        if form.is_valid():
            # Check stock for all items in the cart
            for item in cart:
                product = item['product']
                if product.stock < item['quantity']:
                    messages.error(
                        request,
                        f"Sorry, we don't have enough stock for {
                            product.name}. "
                        f"Available: {product.stock}"
                    )
                    return redirect('cart_detail')

            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()

            # Get the selected instruction from the form
            selected_instruction = request.POST.get('selected_instruction', '')
            order.delivery_instruction = selected_instruction

            order.save()

            # Create order items and reduce stock
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    quantity=quantity
                )
                product.stock -= quantity
                product.save()

            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_price * 100),  # amount in cents
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
        form = OrderCreateForm(user=request.user)

    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'form': form,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
    })


def payment_success(request):
    """
    Handles the success callback from Stripe after a successful payment.
    Updates the order status and clears the cart.
    """
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
            messages.success(request, f"Payment successful! Your order {
                             order.pk} is now being processed.")
            return render(request, 'orders/payment-success.html', {
                "order": order
            })
        else:
            messages.error(request, "Payment was not successful.")
            return render(request, 'orders/payment-failed.html')

    except stripe.error.StripeError as e:  # type: ignore
        # Handle Stripe-specific errors
        messages.error(request, f"An error occurred: {str(e)}")
        return render(request, 'orders/payment-failed.html')

    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}.")
        return render(request, 'orders/payment-failed.html')


@login_required
def order_list(request):
    """
    Displays a list of orders placed by the currently logged-in user.
    """
    orders = request.user.orders.all()
    return render(request, 'orders/order-history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """
    Displays the details of a specific order.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order-detail.html', {'order': order})


@login_required
@require_POST
def cancel_order(request, order_id):
    """
    Handles the cancellation of an order if the order is in a
    cancellable status.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.cancel():
        messages.success(request, f"Order {
                         order.pk} has been successfully cancelled.")
    else:
        messages.error(request, f"Order {order.pk} cannot be cancelled.")

    return redirect('order-detail', order_id=order.pk)
