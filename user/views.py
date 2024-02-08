from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from .actions.RegisterAction import RegisterAction
from .actions.LoginAction import LoginAction
from .actions.VerifyEmailAction import *
from django.conf import settings

class RegisterView(APIView):
    def post(self,request):
        registration_action = RegisterAction(request)
        status,message = registration_action.execute()
        return Response({"status":status,"message":message})

class VerifyEmail(APIView):
    def get(self,request):
        verify_email_action = VerifyEmailAction(request)
        status,message = verify_email_action.execute()
        if status:
            return redirect(settings.FRONTEND_URL+'login/')
        return redirect(settings.FRONTEND_URL+'404_page_not_found/')

class LogInView(APIView):
    def post(self,request):
        login_action = LoginAction(request)
        status,message =login_action.execute()
        return Response({"status":status,"message":message})

