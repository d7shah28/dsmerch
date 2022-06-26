from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    """Reviews given by customers"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(_('Review Header'), max_length=200, blank=True)
    rating = models.DecimalField(_('Rating'), max_digits=2, decimal_places=2, null=True,blank=True)
    comments = models.TextField(_('Review Comment'), blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)



    def __str__(self) -> str:
        return f'{self.rating}'


