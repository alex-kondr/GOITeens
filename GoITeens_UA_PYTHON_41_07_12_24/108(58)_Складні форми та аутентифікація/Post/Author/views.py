from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .models import Author
from .forms import UserForm, LoginForm

# Create your views here.


def add_author(request: HttpRequest):
    if request.method == "POST":
        author = Author(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            bio=request.POST.get("bio"),
            age=request.POST.get("age")
        )
        author.save()
        return redirect("index")
    return render(request, "add_author.html")


def index(request: HttpRequest):
    return render(request, "index.html", dict(authors=Author.objects.all()))


def sign_up(request: HttpRequest):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Вітаємо з реєстрацією!")
            return redirect("index")
        else:
            messages.error(request, f"Помилки: {form.errors}")
    return render(request, "sign_up.html", dict(form=UserForm()))


def sign_in(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            login(request=request, user=user)
            messages.success(request, "Вітаємо в нашій системі!")
            return redirect("index")
        else:
            messages.error(request, form.errors)
    return render(request, "login.html", dict(form=LoginForm()))