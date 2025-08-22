from apis.auth_api import AuthAPI
from apis.user_api import UserAPI


class UserFlowSteps:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        self.auth = AuthAPI(self.api_base_url)
        self.user = UserAPI(self.api_base_url)

    def create_user_get_details(self, email, password):
        response = self.user.create_user(email, email, password)
        return self.user.get_user(response.json()["id"])

    def user_login(self, email, password):
        return self.auth.login(email, password)
