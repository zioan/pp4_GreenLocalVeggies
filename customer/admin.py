from django.contrib import admin
from .models import CustomerUser

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser",
                    "is_courier", "last_login")


admin.site.register(CustomerUser, CustomerAdmin)
