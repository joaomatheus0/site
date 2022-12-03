from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account
from .crud import createuser
from passlib.hash import pbkdf2_sha256
from .crud import createuser
from .crud import c
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout

def index(request):
    if request.method != "POST":
        return render(request, 'index.html')
        
    if request.method == "POST":
        username = request.POST["login"]
        password = request.POST["password"]
        
        authenticated_user = authenticate(username = username, password = password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("dashboard")
        else:
            return redirect("index")
                
def register(request):
    if request.method != "POST":
        return render(request, 'register.html')

    if request.method == "POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        valditation = createuser.CreateUser.mainUser(
            name = username, 
            email = email, 
            phone = phone, 
            password = password, 
            passwordCheck = password1,
            is_trusty = False,
        )

        if valditation[0] == False:
            return render(request, 'register.html',{
                'bol': valditation[0],
                'msg': valditation[1]
            })
        else:
            return redirect("index")

@login_required(login_url='index')
def dashboard(request):
    if request.method != "POST":
        return render(request, 'dashboard.html')

    # Caso o usuário não utilize o sistma será deslogado em 20 minutos
    if request.session.set_expiry(1200):
        return redirect("index")

    return render(request, 'dashboard.html')

@login_required(login_url='index')
def out(request):
    if request.method == 'POST':
        logout(request)
        return redirect("index")

@login_required(login_url='index')
def settings(request):        
    return render(request, 'settings.html')

@login_required(login_url='index')
def add_insta(request):
    if request.method == "POST":
        username = request.POST["login"]
        password = request.POST["password"]
        
        createuser.Socialuser.user(username, password, social_network = "Instagram")
    return render(request, 'addinsta.html')