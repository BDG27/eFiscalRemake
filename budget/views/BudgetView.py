from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from ..models import Budget
from core.views import UtilsView
from store.models import Store
from uuid import uuid4
from datetime import datetime, timedelta
import os

CEO = UtilsView.CEO()

class BudgetView():

    def budget_new(req):
        if(req.method == 'GET'):
            try: 
                user = req.user
                store = Store.objects.get(user_id = user.id)
                return render(req, "budget/new.html", {
                    "CEO": {
                        "pageTitle": CEO['CEO']['pageTitle']+"Novo orçamento"
                    },
                    "store": store,
                    "certificate": uuid4(),
                    'date_today': datetime.now(),
                    'date_validity': datetime.now()+timedelta(days=7),
                    "AXIOS_URL": os.getenv("AXIOS_URL")
                })
            except Exception as error:
                print(error)
                return redirect('dashboard_login')