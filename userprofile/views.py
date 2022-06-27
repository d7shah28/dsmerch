from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import ProfileForm, AddressForm
from base.forms import DivErrorList
from userprofile.models import ShippingAddress

def profile_page(request):
    user = request.user
    print(f"Current user {user}")
    addresses = ShippingAddress.objects.filter(user=user)
    default_address = addresses.get(default=True)
    other_addresses = addresses.filter(default=False)

    if request.method == 'POST':
        u_form = ProfileForm(request.POST, error_class=DivErrorList, instance=user)
        print(u_form)
        if u_form.is_valid():
            u_form.save()
            if u_form.cleaned_data.get('password') != "":
                # user.set_password(u_form.cleaned_data.get('password'))
                # user.save()
                return redirect('login')
            messages.success(request, f'Successfully updated your information')
            return redirect('profile')
    else:
        u_form = ProfileForm(error_class=DivErrorList, instance=user)

    context = {
        'u_form': u_form
    }
    if addresses:
        context["default_add"] = default_address
        context["other_add"] = other_addresses

    return render(request, 'userprofile/profile.html', context)


def edit_address(request, pk):
    user=request.user
    address = ShippingAddress.objects.get(user=user, pk=pk)
    if request.method == 'POST':
        form_class = AddressForm(request.POST, error_class=DivErrorList, instance=address)
        if form_class.is_valid():
            print("VALID")
            form_class.save()
            messages.success(request, f'Successfully Updated Your Address')
            return redirect('edit_address')
        else:
            print("NOT VALID")
    else:
        form_class=AddressForm(error_class=DivErrorList, instance=address)

    context = {
        'form':form_class
    }
    return render(request, 'userprofile/edit_address.html', context)

def remove_address(request):
    user = request.user
