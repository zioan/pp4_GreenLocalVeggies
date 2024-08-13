from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from orders.models import Order


def is_courier(user):
    return user.is_authenticated and user.is_courier


@login_required
@user_passes_test(is_courier)
def courier_dashboard(request):
    shipped_orders = Order.objects.filter(status='shipped')
    return render(request, 'courier/dashboard.html', {
        'orders': shipped_orders
    })


@login_required
@user_passes_test(is_courier)
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, status='shipped')
    return render(request, 'courier/order_detail.html', {'order': order})


@login_required
@user_passes_test(is_courier)
def mark_delivered(request, order_id):
    order = get_object_or_404(Order, id=order_id, status='shipped')
    if request.method == 'POST':
        order.status = 'delivered'
        order.courier = request.user
        order.delivered_at = timezone.now()
        order.save()
        return redirect('courier_dashboard')
    return render(request, 'courier/confirm_delivery.html', {'order': order})
