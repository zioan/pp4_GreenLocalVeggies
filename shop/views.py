from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from cart.cart import Cart

# Create your views here.


def index(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort')
    category = request.GET.get('category')
    availability = request.GET.get('availability')

    products_list = Product.objects.all()

    # Apply search filter if query exists
    if query:
        products_list = products_list.filter(name__icontains=query)

    # Apply category filter
    if category:
        products_list = products_list.filter(category=category)

    # Apply availability filter
    if availability:
        if availability == 'in_stock':
            products_list = products_list.filter(stock__gt=0)
        elif availability == 'out_of_stock':
            products_list = products_list.filter(stock=0)

    # Apply sorting
    if sort == 'price_asc':
        products_list = products_list.order_by('price')
    elif sort == 'price_desc':
        products_list = products_list.order_by('-price')
    elif sort == 'name':
        products_list = products_list.order_by('name')

    # Pagination, 12 products per page
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Get all categories for the filter
    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        "products": products,
        "categories": categories,
        "current_sort": sort,
        "current_category": category,
        "current_availability": availability,
        "search_query": query,
    }

    return render(request, "shop/index.html", context)


def product_details(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    # Get related products (same category, excluding current product)
    related_products = Product.objects.filter(
        category=product.category).exclude(pk=product.pk)[:4]

    step_value = 1

    context = {
        "product": product,
        "step_value": step_value,
        "related_products": related_products,
    }
    return render(request, "shop/product-details.html", context)


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    try:
        quantity = int(request.POST.get('quantity', 1))
        cart.add(product=product, quantity=quantity, update_quantity=True)
        return JsonResponse({
            'status': 'success',
            'message': f"{quantity} {product.unit} of {product.name} added to cart.",
            # You might need to implement this method
            'cart_quantity': cart.get_item_quantity(product.pk),
            'cart_count': len(cart),
        })
    except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid quantity'}, status=400)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')
