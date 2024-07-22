from django.shortcuts import render
from django.db import connections
from django.db.utils import OperationalError
import logging

logger = logging.getLogger(__name__)


class DatabaseConnectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if database connection is available
        try:
            connections['default'].cursor()
        except OperationalError as e:
            logger.error(f"Database connection failed: {e}")
            return render(request, 'shop/500.html', status=500)

        response = self.get_response(request)
        return response
