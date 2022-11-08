from django.db import models

class Measurement(models.TextChoices):
    UN = 1, "UN"
    CX = 2, "CX"
    L = 3, "L"
    CENTO = 4, "Centro"
    GALAO = 5, "GALÃO"
    KG = 6, "KG"
    JG = 7, "JG"
    M = 8, "M"
    PC = 9, "PC"
    PR = 10, "PR"
    BR = 11, "BR"