from django.db import models
from uuid import uuid4
from .StatusModel import Status
from store.models import Store

class Budget(models.Model):
    number = models.BigIntegerField('Número do orçamento', null=False)
    certificate = models.CharField('Certificado', max_length=255, default=uuid4(), null=False, blank=False)
    emissionDate = models.DateTimeField('Data de Emissão', null=False, blank=False, auto_now_add=True)
    validity = models.DateField('Data de validade', null=False, blank=False)
    description = models.TextField('Descrição')
    amount = models.DecimalField('Valor Total', max_digits=15, decimal_places=2, null=False, blank=False)
    subtotal = models.DecimalField('Subtotal', max_digits=15, decimal_places=2, null=False, blank=False)
    discount = models.DecimalField('Desconto', max_digits=15, decimal_places=2, null=False, blank=False)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.EM_NEGOCIACAO)
    store = models.ForeignKey(Store, null=False, verbose_name='Loja', on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçmentos"