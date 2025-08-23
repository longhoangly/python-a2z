import os
import json
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def api_base_url():
    return "https://reqres.in"


@pytest.fixture(scope="session")
def browser():
    isHeadless = os.getenv("HEADLESS", "true").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=isHeadless)  # change to True in CI
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def pytest_sessionstart(session):
    # Define the target directory for allure results
    results_dir = "reports/allure-results"
    os.makedirs(results_dir, exist_ok=True)

    # Environment
    with open(os.path.join(results_dir, "environment.properties"), "w") as f:
        f.write("Env=Staging\n")
        f.write("Browser=Chrome\n")
        f.write("BaseURL=https://reqres.in\n")
        f.write("Tester=Long Ly\n")

    # Executors
    executor_data = {
        "name": "Long Ly",
        "type": "Docker",
        "buildName": "Auto triggered by schedule",
        "buildUrl": "http://localhost/xxx",
        "reportName": "Allure Test Report",
        "reportUrl": "http://localhost/reports/allure-results",
    }

    with open(os.path.join(results_dir, "executor.json"), "w") as f:
        json.dump(executor_data, f, indent=2)

    # Categories
    categories = [
        {
            "name": "Assertion Errors",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*AssertionError.*",
        },
        {
            "name": "Timeouts",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*(Timeout|timed out).*",
        },
        {
            "name": "Element Not Found",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*(NoSuchElement|ElementNotVisible|Element not found).*",
        },
        {
            "name": "500 Server Errors",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*(500|Internal Server Error).*",
        },
        {
            "name": "Connection Issues",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*(ConnectionRefusedError|ConnectionError|ECONNREFUSED).*",
        },
        {
            "name": "Test Broken (Script/Setup)",
            "matchedStatuses": ["broken"],
            "messageRegex": ".*",
        },
        {
            "name": "Unhandled Exception",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*Exception.*",
        },
    ]

    with open(os.path.join(results_dir, "categories.json"), "w") as f:
        json.dump(categories, f, indent=2)
