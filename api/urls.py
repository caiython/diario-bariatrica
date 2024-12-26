from django.urls import path

from . import views

urlpatterns = [
    path("registrodiario/", views.RegistroDiarioCreateView.as_view(),
         name="registro-diario")
]
