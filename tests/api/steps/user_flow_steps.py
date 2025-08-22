from tests.api.apis.auth_api import AuthAPI
from tests.api.apis.user_api import UserAPI
import allure


class UserFlowSteps:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        self.auth = AuthAPI(self.api_base_url)
        self.user = UserAPI(self.api_base_url)

    @allure.step("Create user {username} with password {password}")
    def create_user_get_details(self, username, password):
        response = self.user.create_user(username, username, password)
        return self.user.get_user(response.json()["id"])

    @allure.step("The user {username} login with password {password}")
    def user_login(self, username, password):
        return self.auth.login(username, password)
