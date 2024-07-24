from django import forms
from .models import CustomerUser


class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = CustomerUser
        # fields = ['first_name', 'last_name',
        #           'email', 'address', 'phone', 'zip_code']
        fields = '__all__'

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return password_confirm
