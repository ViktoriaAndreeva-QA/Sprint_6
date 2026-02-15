import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_faq_section(self):
        faq_section = (By.CSS_SELECTOR, "[class*='Home_FAQ']")
        self.scroll_to_element(faq_section)
    
    def click_faq_question(self, question_number):
        question_locator = (By.ID, f"accordion__heading-{question_number}")
        
        self.scroll_to_element(question_locator)

        element = self.find_element(question_locator)
        self.execute_script("arguments[0].click();", element)
    
    def get_faq_answer(self, question_number):
        answer_locator = (By.ID, f"accordion__panel-{question_number}")
        
        if self.is_visible(answer_locator):
            return self.get_text(answer_locator)
        return ""

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)
    
    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_bottom()
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Нажать на логотип Яндекс и переключиться на новую вкладку")
    def click_yandex_logo_and_switch(self):
        self.click(MainPageLocators.YANDEX_LOGO)

        self.wait_for_new_window()

        self.switch_to_last_window()

        self.wait_for_url_contains('dzen.ru', timeout=15)
    
    @allure.step("Проверить видимость логотипа Самоката")
    def is_scooter_logo_visible(self):
        return self.is_visible(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Проверить видимость логотипа Яндекс")
    def is_yandex_logo_visible(self):
        return self.is_visible(MainPageLocators.YANDEX_LOGO)
