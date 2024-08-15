from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from orders.models import Order
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model

User = get_user_model()


def is_staff(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff)
def order_list(request):
    status_filter = request.GET.get('status', '')
    page = request.GET.get('page', 1)

    order_list = Order.objects.all().order_by('-created_at')

    if status_filter:
        order_list = order_list.filter(status=status_filter)

    paginator = Paginator(order_list, 10)  # Show 10 orders per page

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    status_choices = Order.STATUS_CHOICES

    context = {
        'orders': orders,
        'status_choices': status_choices,
        'current_status': status_filter,
        'current_page': page,
    }
    return render(request, 'staff_dashboard/order_list.html', context)


@login_required
@user_passes_test(is_staff)
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    couriers = User.objects.filter(is_courier=True)

    # Preserve filter and pagination info
    current_status = request.GET.get('status', '')
    current_page = request.GET.get('page', '1')

    context = {
        'order': order,
        'couriers': couriers,
        'current_status': current_status,
        'current_page': current_page,
    }
    return render(request, 'staff_dashboard/order_detail.html', context)


@login_required
@user_passes_test(is_staff)
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        courier_id = request.POST.get('courier')

        if new_status in dict(Order.STATUS_CHOICES):
            if new_status == 'shipped' and not courier_id:
                messages.error(
                    request, "Please assign a courier before marking the order as shipped.")
            else:
                if courier_id:
                    courier = get_object_or_404(
                        User, id=courier_id, is_courier=True)
                    order.courier = courier
                order.status = new_status
                order.save()
                messages.success(request, f"Order #{order.id} status updated to {
                                 order.get_status_display()}")
        else:
            messages.error(request, "Invalid status update")

    # Preserve filter and pagination info
    current_status = request.GET.get('status', '')
    current_page = request.GET.get('page', '1')

    return redirect(f"{reverse('staff_dashboard:order_detail', args=[order_id])}?status={current_status}&page={current_page}")
