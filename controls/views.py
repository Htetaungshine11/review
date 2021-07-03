from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Cuser
from django.contrib.auth.forms import UserCreationForm
class uf(UserCreationForm):
    class Meta:
        model = Cuser
        fields = ["email","username","phone_number"]


class register(View):
    def get(self, request):
        return render(request,"registration/register.html",{"form":uf()})

    def post(self, request):
        a = uf(request.POST)
        if (a.is_vaild()):
            a = a.cleaned_data
            a.save()
            return redirect("login")
        else:
            return render(request,"registration/register.html",{"form":a})