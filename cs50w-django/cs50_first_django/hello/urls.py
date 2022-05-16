from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("gayan", views.gayan, name="gayan"),
  path("dulashi", views.dulashi, name="dulashi"),
  path("dula", views.dulashi, name="dula"),
  path("<str:name>", views.greet, name="greet")
]