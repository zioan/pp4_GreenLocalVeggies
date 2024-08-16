from django.contrib import admin
from .models import DeliveryInstruction


@admin.register(DeliveryInstruction)
class DeliveryInstructionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the DeliveryInstruction model.
    """

    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('title', 'instruction', 'user__email')

    # Fields that are read-only in the admin form
    readonly_fields = ('created_at', 'updated_at')

    # Layout configuration for the detail view
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'instruction')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
