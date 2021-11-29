import requests, json

from .util_response import UtilResponse

from arkmedsproject.settings import (
    ARKMEDS_DEV_TOKEN
)

from arkmedsdb.helpers.config_geral_helper import(
    get_dev_token
)

def arkmeds_request(type_request='GET', body={}, url=""):
    try:

        headers = {
            'Authorization' : "JWT "+ARKMEDS_DEV_TOKEN,
            'Content-Type' : 'application/json'
        }

        if type_request == 'GET':

            response = requests.get('https://desenvolvimento.arkmeds.com/api/v2/'+url, headers=headers, params=body)
            
            status_code = response.status_code

            if response.status_code == 200:

                data = json.loads(response.text)

        elif type_request == 'POST':
            
            response = requests.post('https://desenvolvimento.arkmeds.com/api/v2/'+url, data=json.dumps(body), headers=headers)
            
            status_code = response.status_code

            if response.status_code == 200:

                data = json.loads(response.text)

        if status_code == 200:
            return UtilResponse(message="Request realizado com sucesso", success=True, response=data)
        
        return  UtilResponse(message="Erro ao realizar o request")

    except:
        return UtilResponse(message="Erro ao realizar o request")
