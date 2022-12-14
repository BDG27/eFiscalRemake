from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from ..models import Store, State
from django.contrib.auth.decorators import login_required
from core.views import UtilsView
from validate_docbr import CPF, CNPJ
import os, json

CEO = UtilsView.CEO()

class StoreView():

    def index(req):
        return render(req, "store/index.html", {
            # "states": State.choices
        })

    @login_required
    def store(req):
        if(req.method == 'GET'):
            try: 
                user = req.user
                userEmail = user.email
                store = Store.objects.get(user_id = user.id)
                return render(req, "store/view.html", {
                    "CEO": {
                        "pageTitle": CEO['CEO']['pageTitle']+"Minha Empresa"
                    },
                    "store": store,
                    "userEmail": userEmail,
                    "states": State.choices,
                    "AXIOS_URL": os.getenv("AXIOS_URL")
                })
            except Exception as error:
                print(error)
                return redirect('dashboard_login')

    @login_required
    def store_update(req):
        if(req.method == 'PUT'):
            try:
                data = json.loads(req.body.decode('utf-8'))
                storeId = data['storeId']
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
                primaryColor = data['primaryColor']
                secondaryColor = data['secondaryColor']
                terms = data['terms']

                if(len(storeId) < 1): return JsonResponse({"success": False, "message": 'Informe o id da loja'})
                store = Store.objects.filter(id = storeId)
                if(len(store) < 1): return JsonResponse({"success": False, "message": 'Loja n??o encontrada'})
                if(len(corporateName) < 4): return JsonResponse({"success": False, "message": 'Informe a raz??o social'})
                if(len(brandName) < 4): return JsonResponse({"success": False, "message": 'Informe o nome fantasia'})
                if(len(document) < 11): return JsonResponse({"success": False, "message": 'Informe um documento v??lido'})
                if(len(document) == 11): 
                    cpf = CPF()
                    cpf.repeated_digits = False
                    if(not cpf.validate(document)): return JsonResponse({"success": False, "message": 'CPF inv??lido'})
                if(len(document) == 14): 
                    cnpj = CNPJ()
                    cnpj.repeated_digits = False
                    if(not cnpj.validate(document)): return JsonResponse({"success": False, "message": 'CNPJ inv??lido'})
                if(len(postalCode) < 9): return JsonResponse({"success": False, "message": 'CEP inv??lido'})
                if(len(state) < 2): return JsonResponse({"success": False, "message": 'Estado inv??lido'})
                if(len(city) < 2): return JsonResponse({"success": False, "message": 'Informe uma cidade'})
                if(len(district) < 2): return JsonResponse({"success": False, "message": 'Informe um bairro'})
                if(len(street) < 4): return JsonResponse({"success": False, "message": 'Informe um endere??o'})
                if(len(number) < 1): return JsonResponse({"success": False, "message": 'Informe um n??mero'})
                if(len(phone) < 11): return JsonResponse({"success": False, "message": 'Telefone inv??lido'})
                if(len(cellPhone) < 12): return JsonResponse({"success": False, "message": 'Celular inv??lido'})
                if(len(email) < 7): return JsonResponse({"success": False, "message": 'E-mail inv??lido'})
                if(len(primaryColor) < 2): return JsonResponse({"success": False, "message": 'Cor Prim??ria Inv??lida'})
                if(len(secondaryColor) < 2): return JsonResponse({"success": False, "message": 'Cor Secund??ria Inv??lida'})

                #Atualiza os dados do usuario
                user = req.user
                user.email = email.lower()
                user.save()

                # Atualiza os dados da empresa
                store = store[0]
                store.corporateName = corporateName.title()
                store.brandName = brandName.title()
                store.document = document
                store.ie = ie
                store.postalCode = postalCode
                store.state = state
                store.city = city
                store.district = district
                store.street = street
                store.number = number
                store.phone = phone
                store.cellPhone = cellPhone
                store.primaryColor = primaryColor
                store.secondaryColor = secondaryColor
                store.terms = terms
                store.save()

                return JsonResponse({"success": True})
            except Exception as error:
                return JsonResponse({"success": False, "message": str(error)})













