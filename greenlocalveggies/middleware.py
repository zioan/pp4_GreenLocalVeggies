from django.core.exceptions import PermissionDenied


class SuperuserRequiredMiddleware:
    """
    Middleware to restrict access to admin site to superusers only
    and handle PermissionDenied exceptions.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_admin_path = request.path.startswith('/admin/')
        is_not_superuser = not request.user.is_superuser

        if is_admin_path and is_not_superuser:
            raise PermissionDenied
        return self.get_response(request)
