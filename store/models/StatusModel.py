from django.db import models

class Status(models.TextChoices):
    ATIVO = 1, "Ativo"
    INATIVO = 2, "Inativo"