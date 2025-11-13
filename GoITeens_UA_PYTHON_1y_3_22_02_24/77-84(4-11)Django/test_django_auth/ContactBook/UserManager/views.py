from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponseForbidden

from .models import MySuperUser
from .forms import SignUp, Login

# Create your views here.


def sign_up(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")

    form = SignUp(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.add_message(request=request, level=messages.SUCCESS, message="Вітаю з рееєстрацією")
        return redirect("index")

    return render(request, "sign_up.html", {"form": form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("index")

    form = Login(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
        )
        if user:
            login(request=request, user=user)
            messages.add_message(request=request, level=messages.SUCCESS, message="Успішний вхід")
            return redirect("index")
        else:
            messages.add_message(request=request, level=messages.ERROR, message="Мимо!!! Спробуй ще раз")

    return render(request=request, template_name="sign_in.html", context=dict(form=form))


@login_required(login_url="/sign_in/")
def index(request):
    print(request.COOKIES)
    return render(request=request, template_name="index.html")


@login_required(login_url="/sign_in/")
def logout_func(request):
    logout(request)
    messages.success(request, "Ви успішно вийшли")
    return redirect("sign_in")


def get_users(request: HttpRequest):
    if not request.user.is_staff:
        return HttpResponseForbidden()

    users = MySuperUser.objects.all()
    return render(request, "users.html", dict(users=users))
