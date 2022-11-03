from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from ..models import Store, State
from django.contrib.auth.decorators import login_required

class StoreView():

    def index(req):
        return render(req, "store/index.html", {
            # "states": State.choices
        })

    @login_required
    def loja(req):
        return render(req, "store/new.html", {
            "states": State.choices
        })