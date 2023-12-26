from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.auth import logout, authenticate, login as m_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        uname = request.POST.get("username")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same!!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, "sign-up.html")


def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass")

        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            m_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!!")

    return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homepage(request):
    return render(request, "home.html")


@login_required(login_url='login')
def about(request):
    return render(request, "about.html")


@login_required(login_url='login')
def service(request):
    return render(request, "services.html")


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')


@login_required(login_url='login')
def car(request):
    return render(request, "car.html")


@login_required(login_url='login')
def two_wheeler(request):
    return render(request, "two-wheeler.html")
