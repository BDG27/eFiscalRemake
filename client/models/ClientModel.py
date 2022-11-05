from django.db import models
from store.models import State, Status, Store

class Client(models.Model):
    brandName = models.CharField('Nome Fantasia', max_length=255, null=True, blank=True)
    corporateName = models.CharField('Razão Social', max_length=255)
    document = models.CharField('CPF/CNPJ', max_length=100, unique=True, null=True, blank=True)
    ie = models.CharField('IE', max_length=100, null=True, blank=True, unique=True)
    phone = models.CharField('Telefone', max_length=50, null=True, blank=True) 
    cellPhone = models.CharField('Celular', max_length=50, null=True, blank=True)
    email = models.CharField('E-mail', max_length=80, null=True, unique=True, blank=True)
    postalCode = models.CharField('CEP', max_length=50, null=True, blank=True)
    state = models.CharField('Estado', max_length=2, choices=State.choices, null=True, blank=True)
    city = models.CharField('Cidade', max_length=255, null=True, blank=True)
    district = models.CharField('Bairro', max_length=255, null=True, blank=True)
    street = models.CharField('Endereço', max_length=255, null=True, blank=True)
    number = models.CharField('Número', max_length=50, null=True, blank=True)
    observation = models.TextField('Observação', null=True, blank=True) 
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ATIVO) 
    store = models.ForeignKey(Store, null=False, verbose_name='Loja', on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
