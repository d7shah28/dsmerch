from django.shortcuts import redirect, render

from base.models import Product
from orders.models import Order
from .models import Cart
# Create your views here.

def cart_home(request):
    cart_obj, new_obj =  Cart.objects.new_or_get(request)
    context = {
        "cart": cart_obj
    }
    return render(request, "cart/home.html", context)


def cart_update(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        try:
            product_obj = Product.objects.get(_id=product_id)
        except Product.DoesNotExist:
            print("Show message to user that product does not exist") # TODO
            return redirect("cart_home")
    
        cart_obj, new_obj =  Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session["cart_items"] = cart_obj.products.count()

    return redirect('cart_home')

def checkout_page(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart_home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    context = {
        "object": order_obj
    }

    return render(request, "cart/checkout.html", context)