from .neti import NetiClient

class NetiSDK:
    def client(self, model, apikey, endpoint=None):
        return NetiClient(model=model, apikey=apikey, endpoint=endpoint)
