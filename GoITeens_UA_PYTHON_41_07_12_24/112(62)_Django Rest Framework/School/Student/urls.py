from django.urls import path

from . import views


urlpatterns = [
    path('', views.test_models),
    path("api/", views.test_api),
]