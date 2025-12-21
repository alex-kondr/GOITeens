from django.urls import path

from . import views


urlpatterns = [
    path("", views.add_subscription, name="add_subscription"),
    path("activate/", views.activate_subscription, name="activate_subscription")
]
