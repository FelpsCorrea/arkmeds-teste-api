import os

def verifyVariable(var):

    try:
        ambVar = os.environ[var]

        return ambVar

    except:
        return ""