from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404, HttpResponseNotFound
from django.contrib import messages

from .models import Planer
from PhoneBook.models import Contact
from .forms import PlanerForm

# Create your views here.


@login_required
def add_planer(request: HttpRequest):
    form = PlanerForm()
    if request.method == "POST":
        form = PlanerForm(request.POST)
        if form.is_valid():
            planer: Planer = form.save(commit=False)
            planer.user = request.user
            planer.save()
            messages.add_message(request, messages.SUCCESS, "Зустріч успішно створена")
            return redirect("get_planers")

    form.fields["contact"].queryset = Contact.objects.filter(user=request.user).all()
    return render(request, "add_planer.html", dict(form=form))


@login_required
def get_my_planers(request: HttpRequest):
    planers = Planer.objects.filter(user=request.user).all()
    return render(request, "my_planers.html", dict(planers=planers))


@login_required
def get_planers_for_me(request: HttpRequest):
    planers = Planer.objects.filter(contact__first_name=request.user.first_name, contact__last_name=request.user.last_name).all()
    return render(request, "planers_for_me.html", dict(planers=planers))


@login_required
def meet_accept(request: HttpRequest, meet_id: int):
    meet = (Planer.objects
            .filter(id=meet_id)
            .filter(contact__first_name=request.user.first_name)
            .filter(contact__last_name=request.user.last_name)
    ).first()
    if not meet:
        return HttpResponseNotFound()

    meet.accept = True
    meet.save()
    messages.add_message(request, level=messages.SUCCESS, message="Зустріч підтверджена")
    return redirect("get_planers_for_me")


@login_required
def meet_disclaime(request: HttpRequest, meet_id: int):
    meet = (Planer.objects
            .filter(id=meet_id)
            .filter(contact__first_name=request.user.first_name)
            .filter(contact__last_name=request.user.last_name)
    ).first()
    if not meet:
        return HttpResponseNotFound()

    meet.accept = False
    meet.save()
    messages.add_message(request, level=messages.SUCCESS, message="Зустріч анульовано")
    return redirect("get_planers_for_me")
