from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTINUE_BUTTON = (By.ID, "continue")

        self.TOTAL_LABEL = (
            By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(
            self, first_name: str, last_name: str, postal_code: str):
        fn_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME))
        fn_field.clear()
        fn_field.send_keys(first_name)

        ln_field = self.wait.until(EC.visibility_of_element_located(
            self.LAST_NAME))
        ln_field.clear()
        ln_field.send_keys(last_name)

        pc_field = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE))
        pc_field.clear()
        pc_field.send_keys(postal_code)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_btn.click()

    def get_total_price_text(self) -> str:
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                self.TOTAL_LABEL))
        return total_element.text
