from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from llm_model import main
import json
from llm_model.main import generate_answer


class HomeView(LoginRequiredMixin,APIView):
    login_url = '/user/login'
    def get(self,request):
        print("HOme is available")
        return Response({"status":"success","message":"Home page is available"})


class Demo(APIView):
    def get(self,request):
        return Response("JElo")
    
class SendMessage(APIView):
    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            query = data.get("message")
            answer = generate_answer(query=query)
            response_message = f"Bot Response: {answer}."
            return JsonResponse({'message': response_message})
        return JsonResponse({'error': 'Invalid request method'}, status=400)