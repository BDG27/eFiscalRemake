from django.db import models
from .BudgetModel import Budget
from .MeasurementModel import Measurement

class Product(models.Model):
    description = models.TextField('Descrição', null=False)
    measurement = models.CharField(max_length=50, choices=Measurement.choices, null=False)
    quantity = models.FloatField('Quantidade', null=False)
    unityValue = models.DecimalField('Valor Unitário', max_digits=15, decimal_places=2, null=False)
    amount = models.DecimalField('Valor Total', max_digits=15, decimal_places=2, null=False)
    budget = models.ForeignKey(Budget, null=False, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Produto - Orçamento"
        verbose_name_plural = "Produtos - Orçamentos"