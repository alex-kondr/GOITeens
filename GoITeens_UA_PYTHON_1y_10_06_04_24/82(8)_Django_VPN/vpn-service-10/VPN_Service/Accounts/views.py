from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Profile
from .forms import SignIn, SignUp, UserEdit, ProfileForm
from SixSeven_RandomVPN.models import Service, Subscription

# Create your views here.


def sign_up(request: HttpRequest):
    form = SignUp(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user: User = form.save()
        Profile.objects.create(user=user)
        user.details.save()
        messages.info(request, "Вітаю, реєстрація пройшла успішно!")
        return redirect("index")
    return render(request, "sign_up.html", dict(form=form))


def sign_in(request: HttpRequest):
    form = SignIn(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if not user:
            messages.error(request, "Неправильно введені дані")
            return redirect("sign_in")

        login(request, user)
        messages.success(request, "Вхід успішний")
        return redirect("index")
    return render(request, "sign_in.html", dict(form=form))


@login_required
def index(request: HttpRequest):
    # print(f"{request.COOKIES = }")
    print(f"{ request.session.get("testcookie") = }")
    session_id = request.COOKIES.get("sessionid")
    response: HttpResponse = render(request, "index.html")
    # response.delete_cookie("sessionid")
    exp_time = datetime.now() + timedelta(seconds=10)
    # response.set
    response.set_cookie(key="sessionid", value=session_id, expires=exp_time)
    return response


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    messages.success(request, "Ви успішно вийшли із системи.")
    return redirect("sign_in")


@login_required
@require_GET
def profile_user(request: HttpRequest):
    form_user = UserEdit(instance=request.user)
    form_profile = ProfileForm(instance=request.user.details)
    return render(request, "profile.html", dict(form_profile=form_profile, form_user=form_user))


@login_required
@require_POST
def update_profile_user(request: HttpRequest):
    form_user = UserEdit(data=request.POST, instance=request.user)
    form_profile = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.details)

    if form_user.changed_data:
        form_user.save()

    if form_profile.changed_data:
        form_profile.save()

    messages.success(request, "Дані успішно оновлені")
    return redirect("profile_user")


class SubscriptionView(ListView):
    model = Subscription
    paginate_by = 2


def subscriptions_view(request: HttpRequest):
    service = Service.objects.filter(user=request.user).first()
    if service:
        subscriptions = service.subscription.all()

        paginator = Paginator(subscriptions, 2)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)
        return render(request, "SixSeven_RandomVPN/subscription_list.html", dict(page_obj=page_obj))

    messages.info(request, "Ще не оформлено щодної підписки")
    return redirect("index")
