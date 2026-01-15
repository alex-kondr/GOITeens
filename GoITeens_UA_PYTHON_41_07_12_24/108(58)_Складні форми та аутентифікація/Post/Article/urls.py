from django.urls import path

from . import views


urlpatterns = [
    path("add_article/", views.add_article, name="add_article"),
    path("add_article_form/", views.add_article_form, name="add_article_form"),
    path("", views.get_articles, name="get_articles"),
]
