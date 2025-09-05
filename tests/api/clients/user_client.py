from utils.http_client import HttpClient


class UserClient(HttpClient):
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, email, username, password):
        headers = {"x-api-key": "reqres-free-v1"}
        response = self.request(
            path="/api/register",
            headers=headers,
            json_data={
                "email": email,
                "username": username,
                "password": password,
            },
        )
        response.raise_for_status()
        return response

    def get_user(self, user_id):
        headers = {"x-api-key": "reqres-free-v1"}
        response = self.request(
            path=f"/api/users/{user_id}",
            headers=headers,
        )
        response.raise_for_status()
        return response
