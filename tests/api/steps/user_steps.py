import pytest
import allure

from tests.api.clients.auth_client import AuthClient
from tests.api.clients.user_client import UserClient


@pytest.fixture(scope="function")
def user_steps(base_url):
    return UserSteps(base_url)


class UserSteps:
    def __init__(self, base_url):
        self.auth_client = AuthClient(base_url)
        self.user_client = UserClient(base_url)

    @allure.step("Create user {username} with password {password}")
    def create_user(self, username, password):
        response = self.user_client.create_user(username, username, password)
        return self.user_client.get_user(response.json()["id"])

    @allure.step("The user {username} login with password {password}")
    def user_login(self, username, password):
        return self.auth_client.login(username, password)
