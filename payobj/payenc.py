import base64

class PayloadEncryptor(object):
    def changer(payload: str):
        return "powershell -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()
