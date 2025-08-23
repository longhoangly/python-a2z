from tests.api.services.auth_service import AuthService
from tests.api.services.user_service import UserService
import allure


class UserFlowSteps:
    def __init__(self, base_url):
        self.base_url = base_url
        self.auth = AuthService(self.base_url)
        self.user = UserService(self.base_url)

    @allure.step("Create user {username} with password {password}")
    def create_user_get_details(self, username, password):
        response = self.user.create_user(username, username, password)
        return self.user.get_user(response.json()["id"])

    @allure.step("The user {username} login with password {password}")
    def user_login(self, username, password):
        return self.auth.login(username, password)
