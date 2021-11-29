from django.db import models

class Empresa(models.Model):
    id_ref = models.IntegerField("Id da empresa")
    tipo = models.IntegerField("Id do tipo")
    nome =  models.CharField("Nome da empresa", max_length=256)
    nome_fantasia = models.CharField("Nome fantasia da empresa", max_length=256, blank=True)
    superior = models.IntegerField("Id? do superior", null=True)
    cnpj = models.CharField("CNPJ da empresa", max_length=14, blank=True)
    observacoes = models.CharField("Observações da empresa", max_length=256, blank=True)
    contato = models.CharField("Nome do contato da empresa", max_length=256, blank=True)
    email = models.CharField("Email do contato da empresa", max_length=256, blank=True)
    telefone2 = models.CharField("Segundo telefone para contato", max_length=24, blank=True)
    ramal2 = models.CharField("Segundo ramal", max_length=256, blank=True)
    telefone1 = models.CharField("Primeiro telefone para contato", max_length=24, blank=True)
    ramal1 = models.CharField("Primeiro ramal", max_length=256, blank=True)
    fax = models.CharField("Fax da empresa", max_length=256, blank=True)
    cep = models.CharField("CEP da empresa", max_length=25, blank=True)
    rua = models.CharField("Rua da empresa", max_length=256, blank=True)
    numero = models.IntegerField("Numero da empresa", null=True)
    complemento = models.CharField("Complemento da empresa", max_length=128, blank=True)
    bairro = models.CharField("Bairro da empresa", max_length=256, blank=True)
    cidade = models.CharField("Cidade da empresa", max_length=256, blank=True)
    estado = models.CharField("Rua da empresa", max_length=128, blank=True)

    class Meta:
        db_table = 'empresa'