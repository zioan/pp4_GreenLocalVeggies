from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from orders.models import Order


def is_courier(user):
    """
    Check if the user is authenticated and is a courier.

    Args:
        user: The user object to check.

    Returns:
        bool: True if the user is authenticated and is a courier,
            False otherwise.
    """
    return user.is_authenticated and user.is_courier


@login_required
@user_passes_test(is_courier)
def courier_dashboard(request):
    """
    Display the courier dashboard with shipped and delivered orders.

    This view shows a list of orders to be delivered (shipped orders)
    and a list of orders already delivered by the current courier.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response with the courier dashboard.
    """
    # Get all shipped orders, ordered by creation date (newest first)
    shipped_orders = Order.objects.filter(
        status='shipped').order_by('-created_at')

    # Get delivered orders for the current courier (newest first)
    delivered_orders = Order.objects.filter(
        status='delivered', courier=request.user).order_by('-delivered_at')

    return render(request, 'courier/dashboard.html', {
        'shipped_orders': shipped_orders,
        'delivered_orders': delivered_orders
    })


@login_required
@user_passes_test(is_courier)
def order_detail(request, order_id):
    """
    Display details of a specific order for the courier.

    This view shows the details of an order if it's either shipped or
    delivered by the current courier.

    Args:
        request: The HTTP request object.
        order_id: The ID of the order to display.

    Returns:
        A rendered HTML response with the order details or a 404 page if
        the order is not accessible to the courier.
    """
    order = get_object_or_404(Order, id=order_id)

    # Check if the order is either shipped or delivered by the current courier
    if (order.status not in ['shipped', 'delivered'] or
            (order.status == 'delivered' and order.courier != request.user)):
        return render(request, '404.html', status=404)

    return render(request, 'courier/order-detail.html', {'order': order})


@login_required
@user_passes_test(is_courier)
def mark_delivered(request, order_id):
    """
    Mark an order as delivered by the courier.

    This view handles the process of marking an order as delivered. It updates
    the order status, sets the courier, and records the delivery time.

    Args:
        request: The HTTP request object.
        order_id: The ID of the order to mark as delivered.

    Returns:
        A redirect to the courier dashboard after processing or a confirmation
        page if it's a GET request.
    """
    order = get_object_or_404(Order, id=order_id, status='shipped')

    if request.method == 'POST':
        try:
            order.status = 'delivered'
            order.courier = request.user
            order.delivered_at = timezone.now()
            order.save()
            messages.success(request, f'Order #{
                             order.pk} has been marked as delivered.')
        except Exception as e:
            messages.error(request, f'Error marking order as delivered: {e}')
        return redirect('courier_dashboard')

    return render(request, 'courier/confirm-delivery.html', {'order': order})
