from django import forms

class GetDetalheEmpresasForm(forms.Form):
    id_empresa = forms.IntegerField(label="ID da empresa")

class CriarChamadoEquipamentoForm(forms.Form):
    id_equipamento = forms.IntegerField(label="ID do equipamento")
    id_solicitante = forms.IntegerField(label="ID do proprietário do equipamento")
    data_criacao = forms.IntegerField(label="Data em milisegundos")
    tipo_servico = forms.IntegerField(label="Tipo do serviço")
    problema = forms.IntegerField(label="Id do problema")
    id_tipo_ordem_servico = forms.IntegerField(label="Id do tipo da ordem de serviço")

class GetChamadosEquipamentoForm(forms.Form):
    id_equipamento = forms.IntegerField(label="ID do equipamento")