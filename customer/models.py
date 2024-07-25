from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Normalize the email
        email = self.normalize_email(email)

        return self.create_user(email, password, **extra_fields)


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    REQUIRED_ZIP_CODE = [
        ("26655", "26655"),
    ]

    REQUIRED_CITY = [
        ("Westerstede", "Westerstede"),
    ]

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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_user_set',  # Customize the related name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_set',  # Customize the related name
        blank=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
