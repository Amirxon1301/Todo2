from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.method == "POST":
        Reja.objects.create(
            t_name=request.POST.get("t_n"),
            t_detail=request.POST.get("t_d"),
            date=request.POST.get("d"),
            progress=request.POST.get("p"),
            egasi=request.user
        )
        return redirect("/index")
    if request.user.is_authenticated:
        data = {
            "rejalar" : Reja.objects.filter(egasi=request.user)
        }
        return render(request, 'index.html', data)
    return redirect("/")

def edit(request):
    return render(request, 'edit.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username = request.POST.get("l"),
            password = request.POST.get("p")
        )
        if user is  None:
            return redirect("/")
        login(request, user)
        return redirect("/index")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")

def reja_ochir(request, son):
    if request.user.is_authenticated:
        Reja.objects.filter(id=son, egasi=request.user).delete()
    return redirect("/index/")