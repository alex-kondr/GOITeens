from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .models import CustomUser, Profile
from .forms import CustomUserForm, UpdateUserForm, ProfileForm, LoginForm

# Create your views here.


def sign_up(request: HttpRequest):
    form = CustomUserForm(data=request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        messages.success(request, "Вітаємо з реєстрацією")
        return redirect("index")

    return render(request, "sign_up.html", dict(form=form))


def sign_in(request: HttpRequest):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Успішний вхід")
            return redirect("index")

        messages.error(request, "Користувача з такими даними не існує. Зареєструйтесь")
        return redirect("sign_in")
    return render(request, "sign_in.html", dict(form=form))


@login_required
def index(request: HttpRequest):
    return render(request, "index.html")


@login_required
def profile_update(request: HttpRequest):
    user_form = UpdateUserForm(data=request.POST or None, instance=request.user)
    profile_form = ProfileForm(data=request.POST or None, files=request.FILES or None, instance=request.user.profile)
    if request.method == "POST":
        if user_form.is_valid() and user_form.changed_data:
            user_form.save()
        if profile_form.is_valid() and profile_form.changed_data:
            profile_form.save()

        messages.success(request, "Дані успішно оновлено")
        return redirect("profile")

    return render(request, "profile.html", dict(user_form=user_form, profile_form=profile_form))


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("sign_in")
