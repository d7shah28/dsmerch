from cProfile import Profile
from django.shortcuts import redirect, render

from .forms import ProfileForm
# Create your views here.

def profile_page(request):
    user = request.user
    print(f"Current user {user}")
    if request.method == 'POST':
        u_form = ProfileForm(request.POST, instance=user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = ProfileForm(instance=user)

    context = {
        'u_form': u_form
    }

    return render(request, 'userprofile/profile.html', context)