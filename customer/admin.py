from django.contrib import admin
from .models import CustomerUser

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser",
                    "is_courier", "last_login")

    def get_exclude(self, request, obj=None):
        # Exclude fields from the admin form
        exclude = ()
        if obj:
            exclude = ('password', 'last_login', 'groups', 'user_permissions')
        return exclude


admin.site.register(CustomerUser, CustomerAdmin)
