from django.shortcuts import render
from django.http import HttpRequest
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from .models import Category, Actor, Film, Review


# Create your views here.


# def index(request: HttpRequest):
#     reviews = cache.get("reviews")
#     if not reviews:
#         print("Кеш пустий, відбувся запит до БД")
#         reviews = Review.objects.select_related("film", "user").prefetch_related("film__categories")
#         cache.set("reviews", reviews, 10)
#     return render(request, "index.html", dict(reviews=reviews))


@cache_page(5, key_prefix="1")
def index(request: HttpRequest):
    print("Кеш пустий, відбувся запит до БД")
    reviews = Review.objects.select_related("film", "user").prefetch_related("film__categories", "film__actors")
    return render(request, "index.html", dict(reviews=reviews))