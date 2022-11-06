from django.db import models
from django.contrib.auth.models import User
from . import State, Status, PaymentStatus

class Store(models.Model):
    logo = models.CharField(max_length=255, null=True)
    brandName = models.CharField('Nome Fantasia', max_length=255)
    corporateName = models.CharField('Razão Social', max_length=255)
    document = models.CharField('CPF/CNPJ', max_length=100, unique=True)
    ie = models.CharField('IE', max_length=100, null=True, blank=True, unique=True)
    postalCode = models.CharField('CEP', max_length=50)
    state = models.CharField('Estado', max_length=2, choices=State.choices)
    city = models.CharField('Cidade', max_length=255)
    district = models.CharField('Bairro', max_length=255)
    street = models.CharField('Endereço', max_length=255)
    number = models.CharField('Número', max_length=50)
    phone = models.CharField('Telefone', max_length=50) 
    cellPhone = models.CharField('Celular', max_length=50) 
    slugify = models.CharField(max_length=255) 
    primaryColor = models.CharField('Cor Primária', max_length=50) 
    secondaryColor = models.CharField('Cor Secundária', max_length=50) 
    observation = models.TextField('Observação', null=True) 
    terms = models.TextField('Termos', null=True) 
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ATIVO)   
    paymentStatus = models.CharField(max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.PAGO) 
    user = models.OneToOneField(User, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return self.brandName

    class Meta:
        verbose_name = "Loja"
        verbose_name_plural = "Lojas"