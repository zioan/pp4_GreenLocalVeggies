from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class CustomerUserManager(BaseUserManager):
    """
    Custom manager for CustomerUser model.
    Provides methods to create regular users and superusers.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Normalize the email
        email = self.normalize_email(email)

        return self.create_user(email, password, **extra_fields)


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that uses email as the unique identifier
    instead of username.
    """

    # Constants for required fields
    REQUIRED_ZIP_CODE = [
        ("26655", "26655"),
    ]
    REQUIRED_CITY = [
        ("Westerstede", "Westerstede"),
    ]

    # User model fields
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    house_number = models.CharField(max_length=10, blank=False, null=False)
    city = models.CharField(
        max_length=100, choices=REQUIRED_CITY, blank=False, null=False)
    zip_code = models.CharField(
        max_length=5, choices=REQUIRED_ZIP_CODE, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    # Indicates if the user is active
    is_active = models.BooleanField(default=True)
    # Indicates if the user can access the staff dashboard
    is_staff = models.BooleanField(default=False)
    # Indicates if the user can access the courier dashboard
    is_courier = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        default=timezone.now)
    last_login = models.DateTimeField(
        blank=True, null=True)

    # Associate the custom manager
    objects = CustomerUserManager()

    # Field that will be used as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Groups and permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_user_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_set',
        blank=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        # String representation of the user
        return self.email


class CustomerMessage(models.Model):
    """
    Customer message model.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
