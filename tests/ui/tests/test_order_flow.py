from steps.order_flow_steps import OrderFlowSteps

def test_saucedemo_order_flow(page):
    flow = OrderFlowSteps(page)
    flow.complete_order()