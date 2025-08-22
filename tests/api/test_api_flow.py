import requests
import allure
import json


@allure.feature("API Tests")
@allure.story("[Script] create and get user details")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user_flow(api_base_url):
    # Step 1: create a user
    create_response = requests.post(
        f"{api_base_url}/api/register",
        headers={"x-api-key": "reqres-free-v1"},
        json={
            "email": "eve.holt@reqres.in",
            "username": "eve.holt@reqres.in",
            "password": "pistol",
        },
    )
    create_data = create_response.json()
    user_id = create_data["id"]
    print("\n" + json.dumps(create_data, indent=2))

    assert create_response.status_code == 200
    assert "id" in create_data
    assert "token" in create_data

    # Step 2: get created user
    get_response = requests.get(
        f"{api_base_url}/api/users/{user_id}",
        headers={"x-api-key": "reqres-free-v1"},
    )
    get_data = get_response.json()["data"]

    assert get_response.status_code == 200
    print(json.dumps(get_data, indent=2))

    assert get_data["email"] == "eve.holt@reqres.in"
    assert get_data["first_name"] == "Eve"
    assert get_data["last_name"] == "Holt"

    # Step 3: login to get token
    login_response = requests.post(
        f"{api_base_url}/api/login",
        headers={"x-api-key": "reqres-free-v1"},
        json={"email": "eve.holt@reqres.in", "password": "pistol"},
    )
    login_data = login_response.json()
    print(json.dumps(login_data, indent=2))

    assert login_response.status_code == 200
    assert login_data["token"] != None

    print("✅ API test passed successfully.")
