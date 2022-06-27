from doctest import BLANKLINE_MARKER
from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import User

# Create your models here.
class ShippingAddress(models.Model):
    """Shipping Address"""
    BILLING = "BILLING"
    SHIPPING = "SHIPPING"
    TYPE_OF_ADDRESS = [
        (BILLING,'Billing Address'),
        (SHIPPING, 'Shipping Address')
    ]

# Current address
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(_('Address Name'), max_length=100, blank=True, help_text='shipping to')
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10,13}$',
        message='Phone number must be entered in the format +919999999999 \
            Upto 13 digits')
    contact_number = models.CharField(_('Phone Number'), validators=[phone_regex],
        max_length=15,unique=True, null=True, blank=True)
    address_type = models.CharField(_('Address Type'), max_length=100, choices=TYPE_OF_ADDRESS, blank=True)
    address_line_1 = models.CharField(_('Address Line 1'), max_length=120, blank=True)
    address_line_2 = models.CharField(_('Address Line 2'), max_length=120, blank=True)
    city = models.CharField(_('City Name'), max_length=120, blank=True)
    state = models.CharField(_('State Name'), max_length=120, blank=True)
    pincode = models.IntegerField(_('Pincode'), null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name



