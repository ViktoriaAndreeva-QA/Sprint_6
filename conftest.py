import pytest
from selenium import webdriver
from constants import MAIN_PAGE_URL


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_PAGE_URL)
    
    yield driver

    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    """Фикстура для создания экземпляра OrderPage."""
    from pages.order_page import OrderPage
    return OrderPage(driver)

@pytest.fixture(autouse=True)
def cleanup_between_tests(driver):
    yield
    try:
        driver.get(MAIN_PAGE_URL)
    except:
        pass
