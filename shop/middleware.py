from django.shortcuts import render
from django.db import connections
from django.db.utils import OperationalError
import logging

logger = logging.getLogger(__name__)


class DatabaseConnectionMiddleware:
    """
    Middleware that checks the availability of the database connection
    before processing any request.

    If the database connection fails, it logs the error
    and returns the 500 error page.

    This middleware was implemented because CI database was experiencing
    repeated issues during development.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware with the next middleware
        or view in the stack.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Checks the database connection and processes the request.
        If the database connection is unavailable, renders the 500 error page.
        """
        try:
            # Attempt to establish a connection with the database
            connections['default'].cursor()
        except OperationalError as e:
            # Log the error and return a 500 error page if the connection fails
            logger.error(f"Database connection failed: {e}")
            return render(request, 'shop/500.html', status=500)

        # Proceed with the request if the database connection is successful
        response = self.get_response(request)
        return response
