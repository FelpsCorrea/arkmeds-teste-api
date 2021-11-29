from arkmedsdb.models import(
    ConfigGeral
)

def get_dev_token():
    token = ConfigGeral.objects.get(nome='arkmeds-dev-token')
    return token.descricao