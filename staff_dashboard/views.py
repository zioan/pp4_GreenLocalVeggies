from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
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
    order_list = Order.objects.all().order_by('-created_at')

    if status_filter:
        order_list = order_list.filter(status=status_filter)

    page = request.GET.get('page', 1)
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
        'current_status': status_filter
    }
    return render(request, 'staff_dashboard/order_list.html', context)


@login_required
@user_passes_test(is_staff)
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    couriers = User.objects.filter(is_courier=True)
    return render(request, 'staff_dashboard/order_detail.html', {'order': order, 'couriers': couriers})


@login_required
@user_passes_test(is_staff)
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        courier_id = request.POST.get('courier')

        if order.status == 'processing' and new_status == 'shipped':
            if not courier_id:
                messages.error(
                    request, "Please assign a courier before marking the order as shipped.")
            else:
                courier = get_object_or_404(
                    User, id=courier_id, is_courier=True)
                order.courier = courier
                order.status = new_status
                order.save()
                messages.success(request, f"Order #{
                                 order.id} assigned to courier and marked as Shipped")
        else:
            messages.error(request, "Invalid status update")
    return redirect('staff_dashboard:order_detail', order_id=order_id)
