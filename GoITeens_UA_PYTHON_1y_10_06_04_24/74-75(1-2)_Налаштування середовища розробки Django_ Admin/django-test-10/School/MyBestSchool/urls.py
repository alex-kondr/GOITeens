from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_cabinet/", views.add_cabinet, name="add cabinet"),
    path("add_subject/", views.add_subject, name="add subject"),
    path("add_student/", views.add_student, name="add student")
]
