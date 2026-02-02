import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    
    @allure.step("Заполнить форму заказа полностью")
    def fill_order_form(self, data):
        """Заполняет всю форму заказа."""
        
        self.fill_first_page(data)
        
        self.click_next_button()
        
        self.fill_second_page(data)
        
        self.click_order_button()
    
    @allure.step("Заполнить первую страницу")
    def fill_first_page(self, data):
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(data["name"])
        self.find_element(OrderPageLocators.LAST_NAME_INPUT).send_keys(data["last_name"])
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(data["address"])
        
        self.find_element(OrderPageLocators.METRO_INPUT).click()
        station_locator = OrderPageLocators.metro_station(data["metro_station"])
        self.find_element(station_locator).click()
        
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(data["phone"])
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()
    
    @allure.step("Заполнить вторую страницу")
    def fill_second_page(self, data):
        date_field = self.find_element(OrderPageLocators.DATE_INPUT)
        date_field.click()
        date_field.send_keys(data["delivery_date"])
        date_field.send_keys(Keys.ESCAPE)  # Закрываем календарь, если открылся
        
        dropdown = self.find_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        dropdown.click()
        
        period_locator = OrderPageLocators.rental_period(data["rental_period"])
        self.find_element(period_locator).click()
        
        color_locator = OrderPageLocators.color_checkbox(data["color"])
        self.find_element(color_locator).click()
        
        if data["comment"]:
            self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(data["comment"])
    
    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.find_element(OrderPageLocators.ORDER_BUTTON).click()
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.find_element(OrderPageLocators.CONFIRM_YES_BUTTON).click()
    
    @allure.step("Проверить успешное оформление заказа")
    def check_success_message(self):
        success_element = self.find_element(OrderPageLocators.SUCCESS_MESSAGE)
        return success_element.text
