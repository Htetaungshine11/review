from django.urls import path,include
from . import views as v
urlpatterns  = [
    path('',include("django.contrib.auth.urls")),
    path("register/",v.register.as_view(),name="register"),
]