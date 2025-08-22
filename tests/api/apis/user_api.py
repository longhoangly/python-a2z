import requests


class UserAPI:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def create_user(self, email, username, password):
        headers = {"x-api-key": "reqres-free-v1"}
        response = requests.post(
            f"{self.api_base_url}/api/register",
            headers=headers,
            json={
                "email": email,
                "username": username,
                "password": password,
            },
        )
        response.raise_for_status()
        return response

    def get_user(self, user_id):
        headers = {"x-api-key": "reqres-free-v1"}
        response = requests.get(
            f"{self.api_base_url}/api/users/{user_id}",
            headers=headers,
        )
        response.raise_for_status()
        return response
