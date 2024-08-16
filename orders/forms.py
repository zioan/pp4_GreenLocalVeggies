from django import forms
from .models import Order
from delivery_instructions.models import DeliveryInstruction


class OrderCreateForm(forms.ModelForm):
    """
    Form for creating an Order with optional saved delivery instructions.

    Attributes:
        saved_instruction: A dropdown field to select a saved
            delivery instruction.
    """
    saved_instruction = forms.ModelChoiceField(
        queryset=None,
        required=False,
        empty_label="Choose a saved instruction",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Order
        fields = []

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with user-specific delivery instructions.
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Filter delivery instructions based on the current user
            self.fields['saved_instruction'].queryset = (
                DeliveryInstruction.objects.filter(user=user)
            )
        else:
            # No delivery instructions available if no user is provided
            self.fields['saved_instruction'].queryset = (
                DeliveryInstruction.objects.none()
            )
