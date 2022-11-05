from django.db import models

class Status(models.TextChoices):
    EM_NEGOCIACAO = 1, "Em Negociação"
    EM_PRODUCAO = 2, "Em Produção"
    RECUSADO = 3, "Recusado"
    CONCLUIDO = 4, "Concluído"