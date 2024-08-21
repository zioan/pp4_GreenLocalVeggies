from django.contrib import admin
from .models import CustomerUser
from .models import CustomerMessage


class CustomerAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the CustomerUser model.
    """
    list_display = ("email", "is_staff", "is_superuser",
                    "is_courier", "last_login")

    def get_exclude(self, request, obj=None):
        """
        Dynamically exclude fields from the admin form.

        Args:
            request (HttpRequest): The current request object.
            obj (CustomerUser, optional): The object being modified, if any.

        Returns:
            tuple: A tuple of fields to be excluded from the admin form.
        """
        exclude = ()
        if obj:
            exclude = ('password', 'last_login', 'groups', 'user_permissions')
        return exclude


class CustomerMessageAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the CustomerMessage model.
    """
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)


# Register the CustomerUser model with the custom admin configuration
admin.site.register(CustomerUser, CustomerAdmin)

# Register the CustomerMessage model with the custom admin configuration
admin.site.register(CustomerMessage)
