from django.shortcuts import render,redirect

from django.http import HttpResponse


from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
# Create your views here.

def sign_up(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username = username).exists():
            messages.info(request, "username already exists")
            return redirect("/signup/")

        user = User.objects.create(
            username = username,
            email = email
            
        )

        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Succesfully")
        return redirect("/login/")

    return render(request, "signup.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid username")
            return redirect("/login/")
        

        user = authenticate(username = username, password = password)
        
        
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login/")
        

        else:
            login(request, user)
            return redirect("/user_home/")


    return render(request, "login.html")


def user_home(request):
    return render(request, "user_home_page.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")