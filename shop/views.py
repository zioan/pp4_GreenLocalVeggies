from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from cart.cart import Cart


def index(request):
    """
    Renders the main product listing page with optional filters for search,
    category, availability, and sorting. Supports pagination to display
    a limited number of products per page.

    Returns:
        HttpResponse: The rendered 'index.html' page with the list of products.
    """
    query = request.GET.get('q')
    sort = request.GET.get('sort')
    category = request.GET.get('category')
    availability = request.GET.get('availability')

    products_list = Product.objects.all()

    # Apply search filter
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

    # Apply sorting based on user selection
    if sort == 'price_asc':
        products_list = products_list.order_by('price')
    elif sort == 'price_desc':
        products_list = products_list.order_by('-price')
    elif sort == 'name':
        products_list = products_list.order_by('name')

    # Pagination setup to show 12 products per page
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, show the last page
        products = paginator.page(paginator.num_pages)

    # Get all categories for the filter
    categories = Product.objects.values_list(
        'category', flat=True).distinct().order_by('category')

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
    """
    Renders the product detail page for a specific product identified by slug.
    Displays related products from the same category.

    Args:
        request (HttpRequest): The HTTP request object.
        product_slug (str): The slug of the product to retrieve.

    Returns:
        HttpResponse: The rendered 'product-details.html' page with the
            product's details.
    """
    product = get_object_or_404(Product, slug=product_slug)

    # Get related products from the same category, excluding the current one
    # and out-of-stock items
    related_products = Product.objects.filter(
        category=product.category,
        stock__gt=0  # Only include products with stock greater than 0
    ).exclude(pk=product.pk).order_by('?')[:4]

    # Default step value for quantity increment/decrement
    step_value = 1

    context = {
        "product": product,
        "step_value": step_value,
        "related_products": related_products,
    }
    return render(request, "shop/product-details.html", context)


@require_POST
def add_to_cart(request, product_id):
    """
    Adds a product to the shopping cart and returns a JSON response.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to add to the cart.

    Returns:
        JsonResponse: A JSON response indicating the result of the operation.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    try:
        # Get quantity from POST data
        quantity = int(request.POST.get('quantity', 1))
        cart.add(product=product, quantity=quantity, update_quantity=True)
        return JsonResponse({
            'status': 'success',
            'message': f"{quantity} {product.unit} of {product.name} "
            "added to cart.",
            'cart_quantity': cart.get_item_quantity(product.pk),
            'cart_count': len(cart),
        })
    except ValueError:
        # Return an error if the quantity is invalid
        return JsonResponse(
            {'status': 'error', 'message': 'Invalid quantity'},
            status=400
        )


def about(request):
    """
    Renders the 'About' page.

    Returns:
        HttpResponse: The rendered 'about.html' page.
    """
    return render(request, 'shop/about.html')


def contact(request):
    """
    Renders the 'Contact' page.

    Returns:
        HttpResponse: The rendered 'contact.html' page.
    """
    return render(request, 'shop/contact.html')
