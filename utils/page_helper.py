import allure
import functools


def screenshot(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]  # the calling instance
        allure.attach(
            self.page.screenshot(full_page=True),
            name="screenshot before step execution",
            attachment_type=allure.attachment_type.PNG,
        )
        result = func(*args, **kwargs)
        allure.attach(
            self.page.screenshot(full_page=True),
            name="screenshot after step execution",
            attachment_type=allure.attachment_type.PNG,
        )
        return result

    return wrapper
