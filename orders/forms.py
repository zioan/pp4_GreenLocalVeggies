from django import forms
from .models import Order
from delivery_instructions.models import DeliveryInstruction


class OrderCreateForm(forms.ModelForm):
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
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['saved_instruction'].queryset = DeliveryInstruction.objects.filter(user=user)
        else:
            self.fields['saved_instruction'].queryset = DeliveryInstruction.objects.none()
