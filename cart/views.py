from django.shortcuts import redirect, render

from base.models import Product
from orders.models import Order
from userprofile.models import ShippingAddress
from .models import Cart

from userprofile.forms import CreateAddressForm
from base.forms import LoginForm
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
    login_form = LoginForm()
    shipping_form = CreateAddressForm()
    order_obj = None
    address_qs = None
    addresses = None
    default_add = None
    other_add = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart_home")
    # else:
    #     order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    billing_address_id = request.session.get('BILLING_address_id', None)
    shipping_address_id = request.session.get('SHIPPING_address_id', None)

    
    if request.user.is_authenticated:
        user = request.user
        address_qs = ShippingAddress.objects.filter(user=user)

        order_obj, new_order_obj = Order.objects.get_or_create(user=user, cart=cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = ShippingAddress.objects.get(id=shipping_address_id)
            del request.session['SHIPPING_address_id']
        if billing_address_id:
            order_obj.billing_address = ShippingAddress.objects.get(id=billing_address_id)
            del request.session['BILLING_address_id']
        if billing_address_id or shipping_address_id:
            order_obj.save() 
        
        addresses = ShippingAddress.objects.filter(user=user)
        if addresses.count() >= 1:
            default_add = addresses.get(default=True)
            other_add = addresses.filter(default=False)

    if request.method == "POST":
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            del request.session["cart_items"]
            del request.session["cart_id"]
            return redirect("success")        

    context = {
        "object": order_obj,
        "login_form": login_form,
        'address_form': shipping_form,
        "default_add": default_add,
        "other_add": other_add,
        'address_qs': address_qs
    }

    return render(request, "cart/checkout.html", context)


def checkout_finish(request):
    return render(request, "cart/checkout_finish.html")