import allure
import json


@allure.feature("API Tests")
@allure.story("create a user and do user login")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user_and_login(user_steps):

    username = "eve.holt@reqres.in"
    password = "pistol"

    response = user_steps.create_user(username, password)
    print(json.dumps(response.json(), indent=3))

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["email"] == "eve.holt@reqres.in"
    assert data["first_name"] == "Eve"
    assert data["last_name"] == "Holt"

    login_response = user_steps.user_login(username, password)
    login_data = login_response.json()
    print(json.dumps(login_data, indent=2))

    assert login_response.status_code == 200
    assert login_data["token"] != None

    print("✅ API test passed successfully.")


@allure.feature("API Tests")
@allure.story("test allure categories")
@allure.severity(allure.severity_level.BLOCKER)
def test_allure_report_categories():
    assert 1 == 2  # Triggers AssertionError
