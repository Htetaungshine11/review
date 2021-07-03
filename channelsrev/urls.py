from django.urls import path
from .consumer import a
urlpatterns = [ 
    path('<str:name>/',a.as_asgi()),
]