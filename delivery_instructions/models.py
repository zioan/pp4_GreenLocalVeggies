from django.db import models
from django.conf import settings


class DeliveryInstruction(models.Model):
    """
    Model representing a delivery instruction.

    Each delivery instruction is associated with a user and contains
    a title and detailed instruction. Timestamps are automatically
    managed for creation and last update.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='delivery_instructions'
    )
    title = models.CharField(max_length=100)
    instruction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the DeliveryInstruction instance.

        Returns:
            str: A string combining the title and the email of the
                associated user.
        """
        return f"{self.title} - {self.user.email}"
