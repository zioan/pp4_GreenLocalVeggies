from django import forms
from .models import DeliveryInstruction


class DeliveryInstructionForm(forms.ModelForm):
    class Meta:
        model = DeliveryInstruction
        fields = ['title', 'instruction']
