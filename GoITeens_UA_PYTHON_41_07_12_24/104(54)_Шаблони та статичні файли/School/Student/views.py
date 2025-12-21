from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(request: HttpRequest):
    students = [
        {"name": "Andrew", "age": 15, "city": "London"},
        {"name": "Alex", "age": 14, "city": "Odesa"},
        {"name": "Oleg", "age": 15, "city": "Kiyv"},
        {"name": "Vlad", "age": 18, "city": "Dnipro"},
    ]
    context = {
        "students": students,
        "school_name": "LevelUP",
        "city": "Odesa"
    }
    return render(request=request, template_name="index.html", context=context)
