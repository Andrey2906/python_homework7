from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.CART_BUTTON = (
            By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart_by_id(
            self, product_button_id: str):
        button_locator = (By.ID, product_button_id)
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator))
        button.click()

    def go_to_cart(self):
        cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON))
        cart_btn.click()
