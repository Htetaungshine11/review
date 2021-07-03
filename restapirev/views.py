from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from .seralizer import sel
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated,AllowAny
class getdata(LoginRequiredMixin,APIView):
    login_url = "/login"
    # permission_classes =[IsAuthenticated|AllowAny]
    # authentication_classes = [TokenAuthentication]
    def get(self,request):
        a = sel(get_user_model().objects.all(),many=True)
        return Response(data=a.data)