import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data.order_test_data import ORDER_TEST_CASES_FOR_TOP_BUTTON, ORDER_TEST_CASES_FOR_BOTTOM_BUTTON
from constants import BASE_URL


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий оформления заказа")
class TestOrderFlow:
    
    @pytest.mark.parametrize("order_data", ORDER_TEST_CASES_FOR_TOP_BUTTON)
    @allure.title("Заказ через верхнюю кнопку")
    def test_order_from_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        
        main_page.click_top_order_button()
        
        order_page = OrderPage(driver)
        order_page.fill_order_form(order_data)
        order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_success_message_displayed(), \
                "Сообщение об успешном оформлении заказа не отображается"
    
    @pytest.mark.parametrize("order_data", ORDER_TEST_CASES_FOR_BOTTOM_BUTTON)
    @allure.title("Заказ через нижнюю кнопку")
    def test_order_from_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        
        main_page.click_bottom_order_button()
        
        order_page = OrderPage(driver)
        order_page.fill_order_form(order_data)
        order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление заказа"):
            assert order_page.is_success_message_displayed(), \
                "Сообщение об успешном оформлении заказа не отображается"

@allure.feature("Проверка логотипов")
class TestLogoRedirects:
    
    @allure.title("Логотип Самоката ведет на главную страницу")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        
        main_page.click_top_order_button()
        
        main_page.click_scooter_logo()
        
        current_url = main_page.get_current_url()
        assert current_url == BASE_URL, \
            f"Логотип Самоката должен вести на главную, но ведет на: {current_url}"
    
    @allure.title("Логотип Яндекса открывает новую вкладку с Яндексом")
    def test_yandex_logo_open_dzen(self, driver):
        main_page = MainPage(driver)
        
        main_page.click_yandex_logo_and_switch()
        
        current_url = main_page.get_current_url()
        
        assert 'dzen.ru' in current_url, \
            f"Ожидался Яндекс.Дзен, но открылось: {current_url}"

@allure.feature("Проверка элементов главной страницы")
class TestMainPageElements:
    
    @allure.title("Проверка видимости верхней кнопки 'Заказать'")
    def test_top_order_button_visible(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Проверить видимость верхней кнопки"):
            assert main_page.is_visible(MainPageLocators.TOP_ORDER_BUTTON), \
                "Верхняя кнопка 'Заказать' не отображается на странице"
    
    @allure.title("Проверка видимости нижней кнопки 'Заказать'")
    def test_bottom_order_button_visible(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Проверить видимость нижней кнопки"):
            assert main_page.is_visible(MainPageLocators.BOTTOM_ORDER_BUTTON), \
                "Нижняя кнопка 'Заказать' не отображается на странице"
