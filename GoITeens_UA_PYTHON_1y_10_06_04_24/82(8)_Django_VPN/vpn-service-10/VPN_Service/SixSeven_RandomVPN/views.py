from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.contrib import messages
from faker import Faker

from .forms import SubscriptionForm
from .models import Service, Subscription

# Create your views here.

fake = Faker()


@login_required
def add_subscription(request: HttpRequest):
    form = SubscriptionForm(data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        service, _ = Service.objects.get_or_create(user=request.user)

        subscription: Subscription = form.cleaned_data["subscription"]
        if subscription not in service.subscription.all():
            service.subscription.add(subscription)
            messages.success(request, "Нову підписку успішно додано")
        else:
            messages.error(request, "Така підписка вже є у Вашому списку.")

        service.save()
        return redirect("index")
    return render(request, "subcription.html", dict(form=form))


@login_required
def activate_subscription(request: HttpRequest):
    service = Service.objects.filter(user=request.user).first()
    if not service:
        messages.info(request, "Спочатку оформіть підписку")
        return render("add_subscription")

    subscription_name = request.GET.get("subscription_name")
    subscription = get_object_or_404(Subscription, name=subscription_name)
    service.subscription_active = subscription

    service.ipv_4_int = fake.ipv4_private() if "ipv_4_int" in subscription.list_of_service else None
    service.ipv_4_ext = fake.ipv4_public() if "ipv_4_ext" in subscription.list_of_service else None
    service.ipv_6 = fake.ipv6() if "ipv_6" in subscription.list_of_service else None

    service.save()
    return redirect("index")