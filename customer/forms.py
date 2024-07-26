from django import forms
from .models import CustomerUser
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('Phone number must contain only digits.')


class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,  # Optional: Add minimum length requirement
        required=True,
        error_messages={
            'required': 'Password is required',
            'min_length': 'Password must be at least 8 characters long',
        }
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={
            'required': 'Confirm password is required',
        }
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        validators=[validate_numeric],
    )

    class Meta:
        model = CustomerUser
        fields = ['first_name', 'last_name', 'street',
                  'house_number', 'city', 'zip_code', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            "first_name": {
                "required": "Your first name must not be empty",
            },
            "last_name": {
                "required": "Your last name must not be empty",
            },
            "street": {
                "required": "Your street address must not be empty",
            },
            "house_number": {
                "required": "Your house number must not be empty",
            },
            "city": {
                "required": "We only allow orders from Westerstede, please confirm your city",
            },
            "zip_code": {
                "required": "We only allow orders from 26655, please confirm your zip code",
            },
            "email": {
                "required": "Your email address must not be empty, you use it to login",
                "unique": "This email address is already registered, please login",
            },
            "phone_number": {
                "required": "Your phone number must not be empty, we may reach you for delivery",
                "invalid": "Phone number must contain only digits",
            },

        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Password and confirm password validation
        if password and confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data


class CustomerLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={
            'required': 'Email address is required.',
            'invalid': 'Enter a valid email address.'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={
            'required': 'Password is required.',
        }
    )


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['first_name', 'last_name', 'street', 'house_number', 'city', 'zip_code', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            "first_name": {
                "required": "Your first name must not be empty",
            },
            "last_name": {
                "required": "Your last name must not be empty",
            },
            "street": {
                "required": "Your street address must not be empty",
            },
            "house_number": {
                "required": "Your house number must not be empty",
            },
            "city": {
                "required": "We only allow orders from Westerstede, please confirm your city",
            },
            "zip_code": {
                "required": "We only allow orders from 26655, please confirm your zip code",
            },
            "email": {
                "required": "Your email address must not be empty, you use it to login",
                "unique": "This email address is already registered, please login",
            },
            "phone_number": {
                "required": "Your phone number must not be empty, we may reach you for delivery",
            },
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomerUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use. Please supply a different email address.")
        return email
