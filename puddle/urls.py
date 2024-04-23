from django.urls import path
from puddle import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),

]