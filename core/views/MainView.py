from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from store.models import State
import json

class MainView():

    def __CEO():
        return {
            "CEO": {
                "pageTitle": settings.CEO_APP_NAME
            }
        }

    def login(req):
        CEO = MainView.__CEO()
        return render(req, "dashboard/login.html", {
            "CEO": {
                "pageTitle": CEO['CEO']['pageTitle']+"Login"
            }
        })

    def login_authenticate(req):
        if(req.method == 'POST'):
            data = json.loads(req.body.decode('utf-8'))
            email = data['email']
            password = data['password']

            if(len(email) < 5):
                return JsonResponse({"success": False, "message": "E-mail muito pequeno"})
            if(len(password) < 6):
                return JsonResponse({"success": False, "message": "Senha muito pequena"})

            user = authenticate(req, username=email, password=password)
            if user is not None:
                login(req, user)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "message": "Usuário ou Senha inválidos"})