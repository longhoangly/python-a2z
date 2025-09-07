import allure
import functools


def screenshots(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, "page"):
            page = self.page  # page method
            allure.attach(
                page.screenshot(full_page=True),
                name=f">> [{func.__name__}] screenshot before action",
                attachment_type=allure.attachment_type.PNG,
            )
            result = func(self, *args, **kwargs)
            allure.attach(
                page.screenshot(full_page=True),
                name=f">> [{func.__name__}] screenshot after action",
                attachment_type=allure.attachment_type.PNG,
            )
        else:
            first_prop_name = next(iter(vars(self)))
            first_prop = vars(self)[first_prop_name]
            page = first_prop.page  # step method

            with allure.step(f">> [{func.__name__}] screenshot before step"):
                allure.attach(
                    page.screenshot(full_page=True),
                    attachment_type=allure.attachment_type.PNG,
                )
            result = func(self, *args, **kwargs)
            with allure.step(f">> [{func.__name__}] screenshot after step"):
                allure.attach(
                    page.screenshot(full_page=True),
                    attachment_type=allure.attachment_type.PNG,
                )
        return result

    return wrapper
