from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

class SandboxView():

    def index(req):
        return HttpResponse('ola')