from django.shortcuts import render

# Create your views here.

def cart_home(request):
    print(dir(request.session))
    # request.session.session_key
    # request.session.set_expiry(300) # 5 mins
    # key = request.session.session_key
    # print(f"Key: {key}")
    request.session["first_name"] = "First"
    return render(request, "cart/home.html")