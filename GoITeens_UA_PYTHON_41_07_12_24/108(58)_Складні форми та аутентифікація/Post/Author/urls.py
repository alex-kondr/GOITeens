from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_author/", views.add_author, name='add_author'),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.sign_in, name="login"),
]
