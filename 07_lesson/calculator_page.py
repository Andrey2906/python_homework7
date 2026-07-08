from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, "#result")

    def set_delay(self, seconds: int):
        element = self.wait.until(
            EC.visibility_of_element_located(self.delay_input))
        element.clear()
        element.send_keys(str(seconds))

    def click_button(self, label: str):
        locator = (By.XPATH, f"//button[normalize-space()='{label}']")
        button = self.wait.until(
            EC.element_to_be_clickable(locator))
        button.click()

    def get_result(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.result_field))
        return element.text
