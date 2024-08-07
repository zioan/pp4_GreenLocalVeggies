from django import forms
from .models import DeliveryInstruction


class DeliveryInstructionForm(forms.ModelForm):
    saved_instruction = forms.ModelChoiceField(
        queryset=DeliveryInstruction.objects.none(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    delivery_instruction = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    class Meta:
        model = DeliveryInstruction
        fields = ['saved_instruction', 'delivery_instruction']
