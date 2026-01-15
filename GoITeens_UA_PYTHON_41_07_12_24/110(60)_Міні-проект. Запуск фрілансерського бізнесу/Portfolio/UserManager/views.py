from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import SignUpForm, SignInForm, ProfileForm, UserEditForm

# Create your views here.


def sign_up(request: HttpRequest):
    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()

            profile_form = ProfileForm(data=request.POST, files=request.FILES)
            if profile_form.is_valid():
                profile  = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                messages.success(request, "Вітаємо з успішною реєстрацією 🎉")
                return redirect("sign_in")

        messages.error(request, sign_up_form.errors)
        return redirect("sign_up")

    return render(request, "sign_up.html", dict(sign_up_form=sign_up_form, profile_form=profile_form))


def sign_in(request: HttpRequest):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            if user is None:
                messages.error(request, "Даний користувач відсутній у системі 😢")
                return redirect("sign_in")

            login(request, user)
            messages.success(request, "Успішний вхід 😎")
            return redirect("index")

    return render(request, "sign_in.html", dict(form=form))


@login_required
def index(request: HttpRequest):
    return render(request, "index.html")


@login_required
def logout_func(request: HttpRequest):
    logout(request)
    return redirect("sign_in")


@login_required
def profile_edit(request: HttpRequest):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        if user_form.changed_data:
            user_form.save()

        profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if profile_form.changed_data:
            profile_form.save()

        messages.success(request, "Дані успішно оновлено 🎉")
        return redirect("profile_edit")

    return render(request, "profile.html", dict(user_form=UserEditForm(), profile_form=ProfileForm()))