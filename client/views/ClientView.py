from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from ..models import Client
from store.models import State
from django.contrib.auth.decorators import login_required
from core.views import UtilsView
from validate_docbr import CPF, CNPJ
import os, json

CEO = UtilsView.CEO()

class ClientView():

    def client(req, id):
        if(req.method == 'GET'):
            try: 
                user = req.user
                client = Client.objects.get(id = id)
                return render(req, "client/view.html", {
                    "CEO": {
                        "pageTitle": CEO['CEO']['pageTitle']+"Visualizar Cliente"
                    },
                    "client": client,
                    "states": State.choices,
                    "AXIOS_URL": os.getenv("AXIOS_URL")
                })
            except Exception as error:
                print(error)
                return redirect('dashboard_login')

    def client_findByName(req, name):
        if(req.method == 'GET'):
            try:
                clients = Client.objects.filter(corporateName__icontains=name)
                clientList = []
                if(len(clients) > 0):
                    for client in clients:
                        address = ''
                        if(client.street != None and client.number != None and client.district != None and client.city != None and client.state != None):
                            address = '{}, {} - {} - {}/{}'.format(client.street, client.number, client.district, client.city, client.state)
                        clientList.append({
                            "id": client.id, 
                            "name": client.corporateName,
                            "document": client.document,
                            "address": address
                        })

                return JsonResponse({"success": True, "clientList": clientList})
            except Exception as error:
                return JsonResponse({"success": False, "message": str(error)})

    def client_update(req):
        if(req.method == 'PUT'):
            try:
                data = json.loads(req.body.decode('utf-8'))
                clientId = data['clientId']
                corporateName = data['corporateName']
                brandName = data['brandName']
                document = data['document']
                ie = data['ie']
                postalCode = data['postalCode']
                state = data['state']
                city = data['city']
                district = data['district']
                street = data['street']
                number = data['number']
                phone = data['phone']
                cellPhone = data['cellPhone']
                email = data['email']
                observation = data['observation']

                if(len(clientId) < 1): return JsonResponse({"success": False, "message": 'Informe o id do cliente'})
                client = Client.objects.filter(id = clientId)
                if(len(client) < 1): return JsonResponse({"success": False, "message": 'Cliente não encontrada'})
                if(len(corporateName) < 4): return JsonResponse({"success": False, "message": 'Informe a razão social'})

                # Atualiza os dados do cliente
                client = client[0]
                client.corporateName = corporateName.title()
                client.brandName = brandName.title()
                client.document = document
                client.ie = ie
                client.postalCode = postalCode
                client.state = state
                client.city = city
                client.district = district
                client.street = street
                client.email = email
                client.number = number
                client.phone = phone
                client.cellPhone = cellPhone
                client.observation = observation
                client.save()

                return JsonResponse({"success": True})
            except Exception as error:
                return JsonResponse({"success": False, "message": str(error)})