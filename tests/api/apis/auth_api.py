import requests


class AuthAPI:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def login(self, email, password):
        headers = {"x-api-key": "reqres-free-v1"}
        response = requests.post(
            headers=headers,
            url=f"{self.api_base_url}/api/login",
            json={"email": email, "password": password},
        )
        response.raise_for_status()
        return response.json()["token"]
