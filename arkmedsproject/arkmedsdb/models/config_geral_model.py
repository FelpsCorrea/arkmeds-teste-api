from django.db import models

class ConfigGeral(models.Model):

    nome =  models.CharField("Nome da configuração que corresponde", max_length=256)
    descricao = models.CharField("Valor da configuração", max_length=256)

    class Meta:
        db_table = 'config_geral'