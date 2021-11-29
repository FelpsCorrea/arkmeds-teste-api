from django.db import models
from . import Empresa

class Equipamento(models.Model):

    id_ref = models.IntegerField("Id externo do equipamento")
    proprietario = models.ForeignKey(Empresa, verbose_name="Id da empresa", on_delete=models.CASCADE, null=True)
    tipo = models.IntegerField("Tipo do equipamento")
    fabricante = models.CharField("Fabricante do equipamento", max_length=256, blank=True)
    modelo = models.CharField("Modelo do equipamento", max_length=256, blank=True)
    patrimonio = models.CharField("Patrimonio do equipamento", max_length=256, blank=True)
    numero_serie = models.CharField("Numero de serie do equipamento", max_length=14, blank=True)

    class Meta:
        db_table = 'equipamento'