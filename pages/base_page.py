import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Прокрутить страницу до низа")
    def scroll_to_bottom(self):
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def execute_script(self, script, *args):
        """Выполнить JavaScript код."""
        return self.driver.execute_script(script, *args)
    
    @allure.step("Проверить видимость элемента {locator}")
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Подождать открытия новой вкладки")
    def wait_for_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))

    @allure.step("Переключиться на последнюю открытую вкладку")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться URL содержащего '{text}'")
    def wait_for_url_contains(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: text in d.current_url,)

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
