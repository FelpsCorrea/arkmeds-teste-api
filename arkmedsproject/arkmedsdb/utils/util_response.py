class UtilResponse:
    def __init__(self, message="Erro", success=False, response={}):
        self.message = message
        self.success = success
        self.response = response
        return