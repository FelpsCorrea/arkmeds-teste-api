import time
import string
import random

from django.core.exceptions import ObjectDoesNotExist

from arkmedsdb.utils.external_util import(
    arkmeds_request
)

from arkmedsdb.helpers.config_geral_helper import(
    get_dev_token
)

from arkmedsdb.models import(
    Equipamento,
    Empresa,
    Chamado
)


def get_empresas_arkmeds_helper():
    request = arkmeds_request(type_request='GET', url='empresa/')

    if request.success:
        return {
            'success': True,
            'response': request.response
        }
    else:
        return {
            'success': False
        }

def get_detalhe_empresa_arkmeds_helper(id_empresa):
    url = 'company/'+str(id_empresa)
    request = arkmeds_request(type_request='GET', url=url)

    if request.success:
        return {
            'success': True,
            'response': request.response
        }
    else:
        return {
            'success': False
        }

def get_equipamentos_empresa_arkmeds_helper(id_empresa):
    url = 'equipamentos_paginados/?empresa_id='+str(id_empresa)
    request = arkmeds_request(type_request='GET', url=url)

    if request.success:
        return {
            'success': True,
            'response': request.response
        }
    else:
        return {
            'success': False
        }

def criar_chamado_equipamento_arkmeds_helper(body:dict):

    request = arkmeds_request(type_request='POST', url='chamado/novo/', body=body)

    if request.success:
        return {
            'success': True,
            'response': request.response
        }
    else:
        return {
            'success': False
        }

def get_chamados_equipamento_arkmeds_helper(id_equipamento):
    url = 'chamado/?equipamento_id='+str(id_equipamento)
    request = arkmeds_request(type_request='GET', url=url)

    if request.success:
        return {
            'success': True,
            'response': request.response
        }
    else:
        return {
            'success': False
        }


'''
    Função que verifica se o chamado já existe no banco, e caso não exista ele é criado
'''
def verifica_chamados(chamado, equipamento_id): 
    try:
        #Verifica se o chamado já existe no banco
        chamado_obj = Chamado.objects.get(id_ref=chamado['id'])

    except ObjectDoesNotExist:

        chamado_obj = Chamado(
            id_ref=chamado['id'],
            equipamento_id=equipamento_id,
            numero=chamado['numero'],
            prioridade=chamado['prioridade'],
            cor_prioridade=chamado['cor_prioridade'],
            chamado_arquivado=chamado['chamado_arquivado'],
            descricao=chamado['problema_str']
        )

        chamado_obj.save()

'''
    Função que verifica se o equipamento já existe no banco, e caso não exista ele é criado.
    Caso não exista também é criado um chamado para ele.
    Essa função também faz uma requisição de todos chamados que são vinculados com o equipamento
'''
def verifica_equipamento(equipamento, empresa_id, empresa_id_ref):

    try:
        #Verifica se o equipamento já existe no banco
        equipamento_obj = Equipamento.objects.get(id_ref=equipamento['id'])

    except ObjectDoesNotExist:
        #Cria o equipamento caso ele não exista
        equipamento_obj = Equipamento(
            id_ref=equipamento['id'],
            proprietario_id=empresa_id,
            tipo=equipamento['tipo']['id'],
            fabricante=equipamento['fabricante'],
            modelo=equipamento['modelo'],
            patrimonio=equipamento['patrimonio'],
            numero_serie=str(equipamento['numero_serie']),
        )

        equipamento_obj.save()

        #Cria chamado para o equipamento
        #A função de criar o chamado está dentro da condição do objeto não existir pois se o objeto existe o chamado já foi criado
        current_milli_time = lambda: int(round(time.time() * 1000))

        obs = ''
        for x in range(10):
            obs += ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(6))
            obs += " "

        chamado_request_body = {
            "equipamento": equipamento_obj.id_ref,
            "solicitante": empresa_id_ref,
            "tipo_servico": 3,
            "problema": 5,
            "observacoes": obs.strip(),
            "data_criacao": current_milli_time(),
            "id_tipo_ordem_servico": 1
        }

        criar_chamado_equipamento_arkmeds_helper(chamado_request_body)

    #Busca os chamados vinculados ao equipamento
    chamados_response = get_chamados_equipamento_arkmeds_helper(equipamento_obj.id_ref)
    if chamados_response['success']:
        if chamados_response['response']['count'] > 0:
            list_chamados = chamados_response['response']['results']
            for chamado in list_chamados:
                verifica_chamados(chamado, equipamento_obj.id)


'''
    Função que verifica se a empresa já existe no banco, e caso não exista ela é criada.
    Essa função também faz uma requisição de todos equipamentos que estão vinculados com a empresa
'''
def verifica_empresa(empresa_id_ref):

    #Busca os detalhes da empresa
    detalhe_response = get_detalhe_empresa_arkmeds_helper(empresa_id_ref)

    if detalhe_response['success']:

        detalhe_empresa = detalhe_response['response']

        try:
            #Verifica se a empresa já existe no banco
            empresa_obj = Empresa.objects.get(id_ref=detalhe_empresa['id'])

        except ObjectDoesNotExist:
            #Cria a empresa caso ela não exista
            empresa_obj = Empresa(
                id_ref=detalhe_empresa['id'],
                tipo=detalhe_empresa['tipo'],
                nome=detalhe_empresa['nome'],
                nome_fantasia=detalhe_empresa['nome_fantasia'],
                superior=detalhe_empresa['superior'],
                cnpj=detalhe_empresa['cnpj'],
                observacoes=detalhe_empresa['observacoes'] if detalhe_empresa['observacoes'] != None else "",
                contato=detalhe_empresa['contato'],
                email=detalhe_empresa['email'],
                telefone2=detalhe_empresa['telefone2'],
                ramal2=detalhe_empresa['ramal2'],
                telefone1=detalhe_empresa['telefone1'],
                ramal1=detalhe_empresa['ramal1'],
                fax=detalhe_empresa['fax'],
                cep=detalhe_empresa['cep'],
                rua=detalhe_empresa['rua'],
                numero=detalhe_empresa['numero'],
                complemento=detalhe_empresa['complemento'],
                bairro=detalhe_empresa['bairro'],
                cidade=detalhe_empresa['cidade'],
                estado=detalhe_empresa['estado']
            )

            empresa_obj.save()

        #Busca os equipamentos vinculados com a empresa
        equipamentos_response = get_equipamentos_empresa_arkmeds_helper(empresa_obj.id_ref)
        if equipamentos_response['success']:
            if equipamentos_response['response']['count'] > 0:
                list_equipamentos = equipamentos_response['response']['results']

                for equipamento in list_equipamentos:
                    verifica_equipamento(equipamento, empresa_obj.id, empresa_obj.id_ref)

def popular_banco_helper():
    empresas_response = get_empresas_arkmeds_helper()

    if empresas_response['success']:
        #Seleciona no máximo 20 empresas
        list_empresas = empresas_response['response'] if len(empresas_response['response']) < 20 else empresas_response['response'][0:20]

        for empresa in list_empresas:
            verifica_empresa(empresa['id'])



'''
def popular_banco_helper():

    empresas_response = get_empresas_arkmeds_helper()

    if empresas_response['success']:
        #Seleciona no máximo 20 empresas
        list_empresas = empresas_response['response'] if len(empresas_response['response']) < 20 else empresas_response['response'][0:20]

        for empresa in list_empresas:

            #Busca os detalhes da empresa
            detalhe_response = get_detalhe_empresa_arkmeds_helper(empresa['id'])

            if detalhe_response['success']:

                detalhe_empresa = detalhe_response['response']

                try:
                    #Verifica se a empresa já existe no banco

                    empresa_obj = Empresa.objects.get(id_ref=detalhe_empresa['id'])


                except ObjectDoesNotExist:

                    #Cria a empresa caso ela não exista
                    
                    empresa_obj = Empresa(
                        id_ref=detalhe_empresa['id'],
                        tipo=detalhe_empresa['tipo'],
                        nome=detalhe_empresa['nome'],
                        nome_fantasia=detalhe_empresa['nome_fantasia'],
                        superior=detalhe_empresa['superior'],
                        cnpj=detalhe_empresa['cnpj'],
                        observacoes=detalhe_empresa['observacoes'] if detalhe_empresa['observacoes'] != None else "",
                        contato=detalhe_empresa['contato'],
                        email=detalhe_empresa['email'],
                        telefone2=detalhe_empresa['telefone2'],
                        ramal2=detalhe_empresa['ramal2'],
                        telefone1=detalhe_empresa['telefone1'],
                        ramal1=detalhe_empresa['ramal1'],
                        fax=detalhe_empresa['fax'],
                        cep=detalhe_empresa['cep'],
                        rua=detalhe_empresa['rua'],
                        numero=detalhe_empresa['numero'],
                        complemento=detalhe_empresa['complemento'],
                        bairro=detalhe_empresa['bairro'],
                        cidade=detalhe_empresa['cidade'],
                        estado=detalhe_empresa['estado']
                    )

                    empresa_obj.save()

                #Busca os equipamentos vinculados com a empresa
                equipamentos_response = get_equipamentos_empresa_arkmeds_helper(empresa_obj.id_ref)
                if equipamentos_response['success']:

                    if equipamentos_response['response']['count'] > 0:
                        list_equipamentos = equipamentos_response['response']['results']

                        for equipamento in list_equipamentos:
                            try:
                                #Verifica se o equipamento já existe no banco
                                equipamento_obj = Equipamento.objects.get(id_ref=equipamento['id'])

                            except ObjectDoesNotExist:
                                #Cria o equipamento caso ele não exista
                                equipamento_obj = Equipamento(
                                    id_ref=equipamento['id'],
                                    proprietario_id=empresa_obj.id,
                                    tipo=equipamento['tipo']['id'],
                                    fabricante=equipamento['fabricante'],
                                    modelo=equipamento['modelo'],
                                    patrimonio=equipamento['patrimonio'],
                                    numero_serie=str(equipamento['numero_serie']),
                                )

                                equipamento_obj.save()

                                #Cria chamado para o equipamento
                                #A função de criar o chamado está dentro da condição do objeto não existir pois se o objeto existe o chamado já foi criado
                                current_milli_time = lambda: int(round(time.time() * 1000))

                                obs = ''
                                for x in range(10):
                                    obs += ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(6))
                                    obs += " "

                                chamado_request_body = {
                                    "equipamento": equipamento_obj.id_ref,
                                    "solicitante": empresa_obj.id_ref,
                                    "tipo_servico": 3,
                                    "problema": 5,
                                    "observacoes": obs.strip(),
                                    "data_criacao": current_milli_time(),
                                    "id_tipo_ordem_servico": 1
                                }

                                criar_chamado_equipamento_arkmeds_helper(chamado_request_body)

                            #Busca os chamados vinculados ao equipamento
                            chamados_response = get_chamados_equipamento_arkmeds_helper(equipamento_obj.id_ref)
                            if chamados_response['success']:
                                if chamados_response['response']['count'] > 0:
                                    list_chamados = chamados_response['response']['results']

                                    for chamado in list_chamados:
                                        try:
                                            #Verifica se o chamado já existe no banco
                                            chamado_obj = Chamado.objects.get(id_ref=chamado['id'])

                                        except ObjectDoesNotExist:

                                            chamado_obj = Chamado(
                                                id_ref=chamado['id'],
                                                equipamento_id=equipamento_obj.id,
                                                numero=chamado['numero'],
                                                prioridade=chamado['prioridade'],
                                                cor_prioridade=chamado['cor_prioridade'],
                                                chamado_arquivado=chamado['chamado_arquivado'],
                                                descricao=chamado['problema_str']
                                            )

                                            chamado_obj.save()
'''