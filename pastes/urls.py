from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_paste, name="pastes")
]
