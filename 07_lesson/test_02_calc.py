import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result()
    assert result == "15", f"Ожидался результат '15', но получено: '{result}'"
