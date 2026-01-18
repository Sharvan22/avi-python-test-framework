import requests

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        ).json()

    def put(self, endpoint, payload):
        return requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=payload
        ).json()
