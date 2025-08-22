from steps.user_flow_steps import UserFlowSteps
import json


def test_create_user_flow():
    flow = UserFlowSteps()
    username = "eve.holt@reqres.in"
    password = "pistol"

    response = flow.create_user_get_details(username, password)
    flow.user_login(username, password)
    print(json.dumps(response.json(), indent=3))

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Long Ly"
    assert data["job"] == "QA Engineer"
    assert "id" in data
    assert "createdAt" in data
