import requests

class APIClient:
    def __init__(self, base_url="https://reqres.in"):
        self.base_url = base_url
        self.token = None

    def login(self, email, password):
        response = requests.post(f"{self.base_url}/api/login", json={
            "email": email,
            "password": password
        })
        response.raise_for_status()
        self.token = response.json().get("token")
        return self.token

    def post(self, path, json=None, auth=True):
        headers = {}
        if auth and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.post(f"{self.base_url}{path}", json=json, headers=headers)
        response.raise_for_status()
        return response

    def get(self, path, params=None, auth=True):
        headers = {}
        if auth and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.get(f"{self.base_url}{path}", params=params, headers=headers)
        response.raise_for_status()
        return response
