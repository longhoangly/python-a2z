from utils.requests_client import RequestsClient


class AuthService(RequestsClient):
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        headers = {"x-api-key": "reqres-free-v1"}
        response = self.request(
            headers=headers,
            path="/api/login",
            json_data={"email": username, "password": password},
        )
        response.raise_for_status()
        return response
