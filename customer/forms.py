from django import forms
from .models import CustomerUser
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.validators import RegexValidator

# Custom validators for phone number and name fields, suggested by ChatGpt
phone_number_validator = RegexValidator(
    r'^\d+$', 'Phone number must contain only digits.'
)

name_validator = RegexValidator(
    r'^[a-zA-Z\s]+$', 'Names should only contain letters and spaces.'
)


class CustomerRegistrationForm(forms.ModelForm):
    """
    Form for registering a new customer user.
    """
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
        # Ensure phone number contains only digits
        validators=[phone_number_validator],
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
                "required": (
                    "We only allow orders from Westerstede, "
                    "please confirm your city"
                ),
            },
            "zip_code": {
                "required": (
                    "We only allow orders from 26655, "
                    "please confirm your zip code"
                ),
            },
            "email": {
                "required": (
                    "Your email address must not be empty, "
                    "you use it to login"
                ),
                "unique": (
                    "This email address is already registered, "
                    "please login"
                ),
            },
            "phone_number": {
                "required": (
                    "Your phone number must not be empty, "
                    "we may reach you for delivery"
                ),
            }
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and apply validators.
        """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].validators.append(name_validator)
        self.fields['last_name'].validators.append(name_validator)

    def clean(self):
        """
        Custom validation to ensure passwords match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Password and confirm password validation
        if password and confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data


class CustomerLoginForm(AuthenticationForm):
    """
    Form for customer login.
    """
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
    """
    Form for updating customer profile information.
    """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        validators=[name_validator],
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        validators=[name_validator],
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        validators=[phone_number_validator],
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
                "required": (
                    "We only allow orders from Westerstede, "
                    "please confirm your city"
                ),
            },
            "zip_code": {
                "required": (
                    "We only allow orders from 26655, "
                    "please confirm your zip code"
                ),
            },
            "email": {
                "required": (
                    "Your email address must not be empty, "
                    "you use it to login"
                ),
                "unique": (
                    "This email address is already registered, "
                    "please login"
                ),
            },
            "phone_number": {
                "required": (
                    "Your phone number must not be empty, "
                    "we may reach you for delivery"
                ),
            },
        }

    def clean_email(self):
        """
        Ensure the email is unique across the CustomerUser model.

        Returns:
            str: The cleaned email value.

        Raises:
            ValidationError: If the email is already in use by another user.
        """
        email = self.cleaned_data.get('email')
        if (
            CustomerUser.objects.filter(email=email)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise forms.ValidationError(
                "This email is already in use. "
                "Please supply a different email address."
            )
        return email


class CustomerPasswordChangeForm(PasswordChangeForm):
    """
    Form for changing a customer's password.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old Password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )
