from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from orders.models import Order
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    return render(request, 'staff_dashboard/order_detail.html', {'order': order})


@login_required
@user_passes_test(is_staff)
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f"Order #{order.id} status updated to {
                             order.get_status_display()}")
        else:
            messages.error(request, "Invalid status")
    return redirect('staff_dashboard:order_detail', order_id=order_id)
