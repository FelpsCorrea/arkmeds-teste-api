from .external_view import(
    get_empresas_arkmeds,
    get_detalhe_empresa_arkmeds,
    get_equipamentos_empresa_arkmeds,
    criar_chamado_equipamento_arkmeds,
    get_chamados_equipamento_arkmeds,
    popular_banco
)

from .empresa_view import(
    list_empresas,
    get_empresa_mais_equipamentos
)

from .equipamento_view import(
    list_equipamentos,
    get_equipamento_mais_chamados
)

from .chamado_view import(
    list_chamados
)