from django.shortcuts import render


def custom_server_error(request):
    """
    Render a custom 500 error page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response object with a custom 500 error page.
    """
    return render(request, '500.html', status=500)


def cookie_policy(request):
    """
    Render the cookie policy page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response object with the cookie policy page.
    """
    return render(request, 'cookie-policy.html')
