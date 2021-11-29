from django.db import models
from . import Equipamento

class Chamado(models.Model):

    id_ref = models.IntegerField("Id externo do chamado")
    equipamento = models.ForeignKey(Equipamento, verbose_name="Id do equipamento", on_delete=models.CASCADE)
    numero = models.CharField("Numero do chamado", max_length=14, blank=True, default="")
    prioridade = models.IntegerField("Nível de prioridade do chamado", default=1)
    cor_prioridade = models.CharField("Hex da cor da prioridade", max_length=14, blank=True, default="#ffffff")
    chamado_arquivado = models.BooleanField("Chamado arquivado ou não", default=False)
    descricao = models.CharField("Descricao do chamado", max_length=256, blank=True, default="")

    class Meta:
        db_table = 'chamado'