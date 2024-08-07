from django import forms
from .models import Order
from delivery_instructions.models import DeliveryInstruction


class OrderCreateForm(forms.ModelForm):
    delivery_instruction = forms.CharField(
        widget=forms.Textarea, required=False)
    saved_instruction = forms.ModelChoiceField(
        queryset=None, required=False, empty_label="Choose a saved instruction")

    class Meta:
        model = Order
        fields = []  # Add any other fields you want to include

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['saved_instruction'].queryset = DeliveryInstruction.objects.filter(
                user=user)
        else:
            self.fields['saved_instruction'].queryset = DeliveryInstruction.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        saved_instruction = cleaned_data.get('saved_instruction')
        delivery_instruction = cleaned_data.get('delivery_instruction')

        if not saved_instruction and not delivery_instruction:
            raise forms.ValidationError(
                "Please either choose a saved instruction or enter a new one.")

        return cleaned_data
