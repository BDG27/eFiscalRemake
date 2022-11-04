from django.db import models

class PaymentStatus(models.TextChoices):
    PAGO = 1, "Pago"
    EM_ABERTO = 2, "Pagamento Pendente"