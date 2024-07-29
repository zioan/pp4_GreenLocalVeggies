from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from .models import Product

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
    try:
        product = Product.objects.get(slug=product_slug)
        step_value = 0.5 if product.allow_half_units else 1
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, "shop/product-details.html", {
        "product": product,
        "step_value": step_value
    })
