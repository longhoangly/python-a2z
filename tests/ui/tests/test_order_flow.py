from tests.ui.steps.order_flow_steps import OrderFlowSteps
import allure


@allure.feature("UI Tests")
@allure.story("[Steps] login and shopping")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_order_flow(page):
    flow = OrderFlowSteps(page)
    flow.complete_order()