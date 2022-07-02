from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save

import math

from cart.models import Cart
from dsmerch.utils import unique_order_id_generator

# Create your models here.
class Order(models.Model):
    """Order table"""
    # COD = 'COD'
    # CARD = 'CARD'
    # UPI = 'UPI'
    # ONLINE = 'ONLINE'
    # TYPE_OF_PAYMENT = [
    #     (COD, 'Cash On Delivery'),
    #     (CARD, 'Debit / Credit'),
    #     (UPI, 'Upi'),
    #     (ONLINE, 'Online Netbanking'),
    # ]
    NOT_DISPATCHED = 'NOT_DISPATCHED'
    DISPATCHED = 'DISPATCHED'
    OTW = 'OTW'
    DELIVERED = 'DELIVERED'
    TYPE_OF_DELIVERY_STATUS = [
        (NOT_DISPATCHED, 'Not Dispatched'),
        (DISPATCHED, 'Dispatched'),
        (OTW, 'On The Way'),
        (DELIVERED, 'Delivered'),
    ]
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(_("Order ID"), max_length=120, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    delivery_status = models.CharField(_('Delivery Status'), max_length=30, choices=TYPE_OF_DELIVERY_STATUS, blank=True)
    tax_price = models.DecimalField(_('Tax'),default=18.00,  max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(_('Shipping Price'), default=50.00, max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(_(' Total Price'), max_digits=30, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(_('Paid?'), default=False, null=True, blank=True)
    # payment_method = models.CharField(_('Payment method'), max_length=30, choices=TYPE_OF_PAYMENT, default=None, blank=True)
    # paid_at =  models.DateTimeField(auto_now_add=False, null=True, blank=True)
    # delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.order_id}"

    def update_total(self):
        cart_total = self.cart.total
        tax_money = self.tax_price/100.00 * float(cart_total)
        shipping_total = self.shipping_price
        refresh_total = math.fsum([cart_total, shipping_total, tax_money])
        self.total_price = refresh_total
        self.save()
        return refresh_total


def pre_save_create_oder_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_oder_id, sender=Order)

def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count():
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order, sender=Order)
