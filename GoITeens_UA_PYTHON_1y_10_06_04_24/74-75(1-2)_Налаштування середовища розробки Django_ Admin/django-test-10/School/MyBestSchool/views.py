from django.shortcuts import render, redirect

from .models import Cabinet, Subject, Student
from .forms import CabinetForm, SubjectForm, StudentForm

# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def add_cabinet(request):
    form = CabinetForm()
    if request.method == "POST":
        form = CabinetForm(request.POST)
        if form.is_valid():
            cabinet = Cabinet(
                name=form.cleaned_data["name"]
            )
            cabinet.save()
            return redirect("index")
    return render(request=request, template_name="add_cabinet.html", context=dict(form=form))


def add_subject(request):
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = Subject(
                name=form.cleaned_data["name"]
            )
            subject.save()
            return redirect("index")
    return render(request=request, template_name="add_subject.html", context=dict(form=form))


def add_student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                bio=form.cleaned_data["bio"],
                age=form.cleaned_data["age"],
                cabinet=form.cleaned_data["cabinet"]
            )
            student.save()
            student.subjects.set(form.cleaned_data["subjects"])
            student.save()
            return redirect("index")
    return render(request=request, template_name="add_student.html", context=dict(form=form))