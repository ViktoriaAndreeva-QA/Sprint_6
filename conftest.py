import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    yield driver

    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)
