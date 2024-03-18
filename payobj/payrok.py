import payobj.payid
import payobj.paycolor
import pyngrok.ngrok as pyn
import time
import platform
import wget
import os
import json

class PayRok(object):

    def setToken(token: str):
        pyn.set_auth_token(token)
        return True
    
    def stableConnection(method: str = "http", port: int = 8080):
        connectionName = payobj.payid.PayID.makePrivateUID()
        data = pyn.connect(method, port, connectionName)

        print(payobj.paycolor.colors.yellow, json.dumps({
            "url": data.public_url,
            "name": data.name,
            "connectionName": connectionName
        }, indent=4))
        
        while 1:
            try:
                time.sleep(0.8)
            except KeyboardInterrupt:
                pyn.disconnect(data.public_url)
                exit()
    
    def getTunnels():
        return pyn.get_tunnels()
    
    def dls(Platform = platform.system(), output_path = os.getcwd()):
        if Platform == "Linux":
            try:
                wget.download("https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-s390x.tgz")
                return {"error": False, "save_in": output_path, "link_url": "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-s390x.tgz"}
            except Exception as ERROR:
                return {"error": True, "base": ERROR}
            
        elif Platform == "Windows":
            try:
                wget.download("https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip")
                return {"error": False, "save_in": output_path, "link_url": "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"}
            except Exception as ERROR:
                return {"error": True, "base": ERROR}
            
        elif Platform == "Darwin":
            try:
                wget.download("https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.zip")
                return {"error": False, "save_in": output_path, "link_url": "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.zip"}
            except Exception as ERROR:
                return {"error": True, "base": ERROR}
        
    def dockerRunner(token: str = None, port: int = 8080, method: str = "http"):
        os.system(f"docker run -it -e NGROK_AUTHTOKEN={token} ngrok/ngrok {method} {port}")
