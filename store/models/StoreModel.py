from django.db import models
from . import State, Status, PaymentStatus

class Store(models.Model):
    logo = models.CharField(max_length=255, null=True)
    brandName = models.CharField(max_length=255)
    corporateName = models.CharField(max_length=255)
    document = models.CharField(max_length=100, unique=True)
    ie = models.CharField(max_length=100, null=True, unique=True)
    postalCode = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=State.choices)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    phone = models.CharField(max_length=50) 
    cellPhone = models.CharField(max_length=50) 
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255) 
    slugify = models.CharField(max_length=255) 
    primaryColor = models.CharField(max_length=50) 
    secondaryColor = models.CharField(max_length=50) 
    observation = models.TextField(null=True) 
    terms = models.TextField(null=True) 
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ATIVO)   
    paymentStatus = models.CharField(max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.PAGO) 

    def __str__(self):
        return self.brandName