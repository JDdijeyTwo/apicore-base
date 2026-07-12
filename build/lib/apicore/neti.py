import requests

class NetiClient:
    def __init__(self, model, key, endpoint=None):
        self.model = model
        self.key = key
        self.endpoint = endpoint or "https://JDdijeyTwo.pythonanywhere.com/v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        })

    def response(self, messages, **kwargs):
        payload = {
            "model": self.model,
            "messages": messages,
            **kwargs
        }
        resp = self.session.post(f"{self.endpoint}/chat/completions", json=payload)
        if resp.status_code != 200:
            raise Exception(f"NetI error: {resp.text}")
        data = resp.json()
        return data["choices"][0]["message"]["content"]
