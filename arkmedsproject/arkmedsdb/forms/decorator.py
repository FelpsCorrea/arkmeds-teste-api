from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
)

from .external_form import *
from .general_form import *

def form_validator(form_str):
    def form_function(function):
        def wrapper(request):

            try:
                
                if request.method in form_str:

                    FormValidator = eval(form_str[request.method])

                    if request.method != 'POST':
                        params = request.query_params
                    else:
                        params = request.data

                    form = FormValidator(params)

                    if not form.is_valid():
                        return Response(
                            {
                                "status" : "Error",
                                "message" : "Os parâmetros para o Request estão inválidos",
                                "Errors" : form.errors
                            }
                        , HTTP_400_BAD_REQUEST)

            except:
                return Response(
                    {
                        "status" : "Error",
                        "message" : "Os parâmetros para o Request estão inválidos"
                    }
                , HTTP_400_BAD_REQUEST)

            return function(request)
        
        return wrapper
    
    return form_function