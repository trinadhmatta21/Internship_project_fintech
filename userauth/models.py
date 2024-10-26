# userauth/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from datetime import timedelta
import random
import string
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Additional fields can be added here
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin
    is_superuser = models.BooleanField(default=False)  # Required for superuser

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
# userauth/models.py
class IPO(models.Model):
    company_logo = models.ImageField(upload_to='company_logos/')
    company_name = models.CharField(max_length=255)
    price_band = models.CharField(max_length=100)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.DecimalField(max_digits=15, decimal_places=2)
    issue_type = models.CharField(max_length=100)
    listing_date = models.DateField()
    status = models.CharField(max_length=50)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_gain = models.DecimalField(max_digits=10, decimal_places=2)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_return = models.DecimalField(max_digits=10, decimal_places=2)
    rhp_pdf = models.FileField(upload_to='rhp_pdfs/')
    drhp_pdf = models.FileField(upload_to='drhp_pdfs/')

    def __str__(self):
        return self.company_name

