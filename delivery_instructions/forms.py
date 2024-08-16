from django import forms
from .models import DeliveryInstruction


class DeliveryInstructionForm(forms.ModelForm):
    """
    Form for creating or updating DeliveryInstruction instances.
    """

    class Meta:
        model = DeliveryInstruction
        fields = ['title', 'instruction']
