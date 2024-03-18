import uuid

class PayID(object):
    def makePrivateUID():
        return uuid.uuid4().hex
    
    def isUID(uid: str = None):
        try:
            uuid.UUID(uid)
            return True
        except:
            return False