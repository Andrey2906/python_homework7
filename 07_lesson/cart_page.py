from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.CHECKOUT_BUTTON = (By.ID, "checkout")
        self.CART_ITEMS = (
            By.CLASS_NAME, "inventory_item_name")

    def get_item_names(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_ITEMS))
        elements = self.driver.find_elements(
            *self.CART_ITEMS)
        return [element.text for element in elements]

    def click_checkout(self):
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
