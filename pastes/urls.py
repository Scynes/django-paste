from django.urls import path
from . import views

urlpatterns = [
    path('', views.PasteUploadView.as_view(), name='upload'),
    path('<str:id>', views.PasteView.as_view(), name='view')
]