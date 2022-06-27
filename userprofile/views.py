from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ProfileForm
from base.forms import DivErrorList
# Create your views here.


def profile_page(request):
    user = request.user
    print(f"Current user {user}")
    if request.method == 'POST':
        u_form = ProfileForm(request.POST, error_class=DivErrorList, instance=user)
        if u_form.is_valid():
            u_form.save()
            if u_form.cleaned_data.get('password'):
                user.set_password(u_form.cleaned_data.get('password'))
                user.save()
                return redirect('login')
            messages.success(request, f'Successfully updated your information')
            return redirect('profile')
    else:
        u_form = ProfileForm(error_class=DivErrorList, instance=user)

    context = {
        'u_form': u_form
    }

    return render(request, 'userprofile/profile.html', context)