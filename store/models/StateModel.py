from django.db import models

class State(models.TextChoices):
    AC = "AC", "Acre" 
    AL = "AL", "Alagoas"
    AP = "AP", "Amapá"
    BA = "BA", "Bahia"
    CE = "CE", "Ceará"
    DF = "DF", "Distrito Federal"
    ES = "ES", "Espírito Santo"
    GO = "GO", "Goiás"
    MA = "MA", "Maranão"
    MG = "MG", "Minas Gerais"
    MS = "MS", "Mato Grosso do Sul"
    MT = "MT", "Mato Grosso"
    PA = "PA", "Pará"
    PB = "PB", "Paraíba"
    PE = "PE", "Pernanbuco"
    PI = "PI", "Piauí"
    PR = "PR", "Paraná"
    RJ = "RJ", "Rio de Janeiro"
    RN = "RN", "Rio Grande do Norte"
    RO = "RO", "Rondônia"
    RR = "RR", "Roraima"
    RS = "RS", "Rio Grande do Sul"
    SC = "SC", "Santa Catarina"
    SE = "SE", "Sergipe"
    SP = "SP", "São Paulo"
    TO = "TO", "Tocantins"