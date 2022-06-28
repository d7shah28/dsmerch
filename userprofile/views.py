from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import (
    ProfileForm, 
    EditAddressForm,
    CreateAddressForm)
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


def create_address(request):
    user = request.user
    if request.method == 'POST':
        form_class = CreateAddressForm(request.POST or None, error_class=DivErrorList, instance=user)
        if form_class.is_valid():
            print(form_class.__dict__)
            obj = form_class.save()
            # obj.save()
            print(f"obj {obj}")
            messages.success(request, f"Successfully created new address")
            return redirect('profile')
    else:
        form_class = CreateAddressForm(error_class=DivErrorList, instance=user)

    context = {
        'form': form_class
    }
    return render(request, 'userprofile/create_address.html', context)


def edit_address(request, pk):
    user=request.user
    address = ShippingAddress.objects.get(user=user, pk=pk)
    if request.method == 'POST':
        form_class = EditAddressForm(request.POST, error_class=DivErrorList, instance=address)
        if form_class.is_valid():
            print("VALID")
            form_class.save()
            messages.success(request, f'Successfully Updated Your Address')
            return redirect('edit_address')
        else:
            print("NOT VALID")
    else:
        form_class=EditAddressForm(error_class=DivErrorList, instance=address)

    context = {
        'form':form_class
    }
    return render(request, 'userprofile/edit_address.html', context)


def make_default_address(request, pk):
    user = request.user
    curr_default_address = ShippingAddress.objects.get(default=True)
    curr_default_address.default = False
    curr_default_address.save()

    new_default_address = ShippingAddress.objects.get(pk=pk)
    new_default_address.default = True
    new_default_address.save()
    return redirect('profile')

def remove_address(request, pk):
    user = request.user
    address = ShippingAddress.objects.get(pk=pk)
    address.delete()
    return redirect('profile')
