from django.urls import path

from . import views


urlpatterns = [
    path("add_meet/", views.add_planer, name="add_meet"),
    path("get_planers/", views.get_my_planers, name="get_planers"),
    path("get_planers_for_me/", views.get_planers_for_me, name="get_planers_for_me"),
    path("meet_accept/<int:meet_id>/", views.meet_accept, name="meet_accept"),
    path("meet_disclaime/<int:meet_id>/", views.meet_disclaime, name="meet_disclaime"),
]
