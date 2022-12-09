from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account, SocialAccount
from .crud import createuser
from .crud import createuser
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from .instagram import instagram

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
    conta = []
    insta = SocialAccount.objects.all()

    # Verifica todas as contas de instagram que tem e coloca em uma lista
    for i in insta:
        if i.account.all().get() == request.user:
            conta.append(str(i))

    if request.method != "POST":        
        return render(request, 'dashboard.html', {
            'insta': insta,
            'conta': conta
            }
        )

    #ASDASDASDAS

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
        account = request.user
        
        # Realizar uma verificação e tratamento do contas não validas.
        if instagram.Login.validation_login(username, password):
            createuser.Socialuser.user_instagram(username, password, social_network = "Instagram", account=account)
            return redirect('dashboard')
        else:
            return redirect('addinsta')
        

    return render(request, 'addinsta.html')