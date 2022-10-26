from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from ..models import Store

class StoreView():

    def index(req):
        return HttpResponse('loja')