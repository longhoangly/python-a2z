import pytest
import allure

from tests.ui.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_steps(page):
    return LoginSteps(page)


class LoginSteps:
    def __init__(self, page):
        self.login_page = LoginPage(page)

    @allure.step("login with {username} and password {pwd}")
    def login(self, username, pwd):
        self.login_page.load()
        self.login_page.login(username, pwd)
