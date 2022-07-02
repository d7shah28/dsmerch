from django.shortcuts import redirect, render

from base.models import Product

from .models import Cart
# Create your views here.

def cart_home(request):
    # request.session["cart_id"] = 13
    print("Cart ID", request.session.get("cart_id"))
    cart_obj, new_obj =  Cart.objects.new_or_get(request)
    return render(request, "cart/home.html")


def cart_update(request):
    product_obj = Product.objects.get(pk=1) # rivia
    cart_obj, new_obj =  Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)

    return redirect('cart_home')