from tests.api.steps.user_flow_steps import UserFlowSteps
import allure
import json

@allure.feature("API Tests")
@allure.story("[Steps] create and get user details")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user_flow(base_url):
    flow = UserFlowSteps(base_url)
    username = "eve.holt@reqres.in"
    password = "pistol"

    response = flow.create_user_get_details(username, password)
    print(json.dumps(response.json(), indent=3))

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["email"] == "eve.holt@reqres.in"
    assert data["first_name"] == "Eve"
    assert data["last_name"] == "Holt"

    login_response = flow.user_login(username, password)
    login_data = login_response.json()
    print(json.dumps(login_data, indent=2))

    assert login_response.status_code == 200
    assert login_data["token"] != None

    print("✅ API test passed successfully.")
