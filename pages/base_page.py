import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу {self.url}")
    def open(self):
        self.driver.get(self.url)
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Прокрутить до элемента {locator}")
    def scroll_to(self, locator):
        element = self.find_element(locator)
        element.location_once_scrolled_into_view
    
    @allure.step("Проверить видимость элемента {locator}")
    def is_visible(self, locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False
