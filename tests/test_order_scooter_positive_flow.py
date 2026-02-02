import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.order_test_data import ORDER_TEST_DATA


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий оформления заказа")
class TestOrderFlow:
    
    TEST_CASES = ORDER_TEST_DATA
    
    @pytest.mark.parametrize("test_case", TEST_CASES)
    @allure.title("Позитивный сценарий заказа самоката")
    def test_order_scooter_positive_flow(self, driver, test_case):
        main_page = MainPage(driver)
        
        with allure.step(f"Нажать на кнопку 'Заказать' ({test_case['button']})"):
            if test_case["button"] == "top":
                main_page.click_top_order_button()
            else:
                main_page.click_bottom_order_button()
        
        with allure.step("Заполнить форму заказа"):
            order_page = OrderPage(driver)
            order_page.fill_order_form(test_case["data"])
        
        with allure.step("Подтвердить заказ в модальном окне"):
            order_page.confirm_order()
        
        with allure.step("Проверить успешное оформление заказа"):
            success_message = order_page.check_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Ожидалось сообщение об успешном оформлении, получено: {success_message}"
            
            allure.attach(
                success_message,
                name="Сообщение об успехе",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Закрыть модальное окно успеха"):
            try:
                driver.refresh()
            except:
                pass

    @allure.title("Проверка редиректов по логотипам")
    def test_logo_redirects(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Проверить логотип Самоката"):
            main_page.click_top_order_button()
            
            main_page.click_scooter_logo()
            
            current_url = driver.current_url
            assert current_url == "https://qa-scooter.praktikum-services.ru/", \
                f"Логотип Самоката должен вести на главную, но ведет на: {current_url}"
        
        with allure.step("Проверить логотип Яндекса"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
            main_page.click_yandex_logo()

            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            
            driver.switch_to.window(driver.window_handles[-1])

            WebDriverWait(driver, 10).until(
                lambda d: d.current_url != 'about:blank'
            )
            
            yandex_url = driver.current_url
            
            driver.close()
            
            driver.switch_to.window(driver.window_handles[0])
            
            assert any(domain in yandex_url for domain in ['dzen.ru', 'yandex.ru']), \
                f"Ожидался Яндекс.Дзен, но открылось: {yandex_url}"

    @allure.title("Проверка обеих кнопок заказа")
    def test_both_order_buttons_exist(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Проверить верхнюю кнопку"):
            assert main_page.is_element_visible(MainPageLocators.TOP_ORDER_BUTTON), \
                "Верхняя кнопка 'Заказать' не найдена"
        
        with allure.step("Прокрутить и проверить нижнюю кнопку"):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            assert main_page.is_element_visible(MainPageLocators.BOTTOM_ORDER_BUTTON), \
                "Нижняя кнопка 'Заказать' не найдена"
