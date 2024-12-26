from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:year>/<int:month>/<int:day>/",
         views.IndexView.as_view(), name="index"),
]
