from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Product
from cart.cart import Cart

# Create your views here.


def index(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort')
    category = request.GET.get('category')
    products_list = Product.objects.all()

    # Apply search filter if query exists
    if query:
        products_list = products_list.filter(name__icontains=query)

    # Apply category filter
    if category:
        products_list = products_list.filter(category=category)

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


def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            messages.error(request, "Invalid quantity.")
            return redirect('product-details', product_slug=product.slug)

        if quantity <= 0 or quantity > product.stock:
            messages.error(request, "Invalid quantity.")
            return redirect('product-details', product_slug=product.slug)

        cart.add(product=product, quantity=quantity, update_quantity=True)

        messages.success(request, f"{quantity} {product.unit} of {
                         product.name} added to cart.")
        return redirect('product-details', product_slug=product.slug)

    return redirect('index')
