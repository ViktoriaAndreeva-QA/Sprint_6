import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_faq_section(self):
        faq_section = (By.CLASS_NAME, "Home_FAQ__3uVm4")
        self.scroll_to(faq_section)
    
    def click_faq_question(self, question_number):
        question_locator = (By.ID, f"accordion__heading-{question_number}")
        
        self.scroll_to(question_locator)

        self.click(question_locator)
    
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
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
    
    def is_element_visible(self, locator):
        return super().is_visible(locator)
    