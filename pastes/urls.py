from django.urls import path
from . import views

urlpatterns = [
    path('', views.PasteUploadView.as_view())
]