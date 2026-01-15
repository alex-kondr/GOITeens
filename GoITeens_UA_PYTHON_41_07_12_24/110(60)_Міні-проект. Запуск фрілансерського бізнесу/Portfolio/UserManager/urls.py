from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.sign_in, name="login"),
    path("profile/", views.profile_edit, name="profile"),
    path("logout/", views.logout_func, name="logout")
]
