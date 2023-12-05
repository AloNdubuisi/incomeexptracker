from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

app_name = ""
urlpatterns = [
    
]

# Create your views here.

def index(request):
    return render(request, 'income_expense_app/index.html',{})


def about(request):
    return render(request, 'income_expense_app/about.html',{})


def services(request):
    return render(request, 'income_expense_app/services.html',{})


def team(request):
    return render(request, 'income_expense_app/team.html',{})

    
def why(request):
    return render(request, 'income_expense_app/why.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('User does not exist')
            
    return render(request, 'income_expense_app/login.html',{})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.firstname = first_name
        new_user.lastname = first_name
        new_user.save()
        
        return redirect('login_user')
    return render(request, 'income_expense_app/register.html',{})


def logout_user(request):
    logout(request)
    return redirect('/')

def reset_password(request):
    return render(request, 'income_expense_app/reset_password.html',{})

def set_new_password(request):
    return render(request, 'income_expense_app/set_new_password.html',{})

login_required
def dashboard(request):
    return render(request, 'income_expense_app/dashboard.html',{})