"""Тесты для раздела 'Вопросы о важном'."""

import allure
from pages.main_page import MainPage


@allure.feature("FAQ раздел")
class TestFAQ:

    def setup_method(self):
        pass
    
    def teardown_method(self):
        pass


    # Тест для вопроса 1
    @allure.title("Вопрос 1: Стоимость аренды")
    def test_question_1_cost(self, driver):
        """Сколько это стоит? И как оплатить?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 1"):
            page.click_faq_question(0)
        
        with allure.step("Получить ответ на вопрос 1"):
            actual_answer = page.get_faq_answer(0)
            expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 1 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 2
    @allure.title("Вопрос 2: Несколько самокатов")
    def test_question_2_multiple_scooters(self, driver):
        """Хочу сразу несколько самокатов! Так можно?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 2"):
            page.click_faq_question(1)
        
        with allure.step("Получить ответ на вопрос 2"):
            actual_answer = page.get_faq_answer(1)
            expected_answer = (
                "Пока что у нас так: один заказ — один самокат. "
                "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
            )
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 2 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 3
    @allure.title("Вопрос 3: Расчет времени аренды")
    def test_question_3_rental_time(self, driver):
        """Как рассчитывается время аренды?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 3"):
            page.click_faq_question(2)
        
        with allure.step("Получить ответ на вопрос 3"):
            actual_answer = page.get_faq_answer(2)
            expected_answer = (
                "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
            )
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 3 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 4
    @allure.title("Вопрос 4: Заказ на сегодня")
    def test_question_4_order_today(self, driver):
        """Можно ли заказать самокат прямо на сегодня?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 4"):
            page.click_faq_question(3)
        
        with allure.step("Получить ответ на вопрос 4"):
            actual_answer = page.get_faq_answer(3)
            expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 4 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 5
    @allure.title("Вопрос 5: Продление аренды")
    def test_question_5_extend_rental(self, driver):
        """Можно ли продлить заказ или вернуть самокат раньше?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 5"):
            page.click_faq_question(4)
        
        with allure.step("Получить ответ на вопрос 5"):
            actual_answer = page.get_faq_answer(4)
            expected_answer = (
                "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 5 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 6
    @allure.title("Вопрос 6: Зарядка самоката")
    def test_question_6_charging_with_scooter(self, driver):
        """Вы привозите зарядку вместе с самокатом?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 6"):
            page.click_faq_question(5)
        
        with allure.step("Получить ответ на вопрос 6"):
            actual_answer = page.get_faq_answer(5)
            expected_answer = (
                "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
            )
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 6 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 7
    @allure.title("Вопрос 7: Отмена заказа")
    def test_question_7_cancel_order(self, driver):
        """Можно ли отменить заказ?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 7"):
            page.click_faq_question(6)
        
        with allure.step("Получить ответ на вопрос 7"):
            actual_answer = page.get_faq_answer(6)
            expected_answer = (
                "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
            )
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 7 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
    
    # Тест для вопроса 8
    @allure.title("Вопрос 8: Доставка за МКАД")
    def test_question_8_delivery_outside_mkad(self, driver):
        """Я живу за МКАДом, привезёте?"""
        page = MainPage(driver)
        
        with allure.step("Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step("Кликнуть на вопрос 8"):
            page.click_faq_question(7)
        
        with allure.step("Получить ответ на вопрос 8"):
            actual_answer = page.get_faq_answer(7)
            expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        
        with allure.step("Проверить ответ"):
            assert actual_answer, "Ответ на вопрос 8 пустой"
            assert actual_answer == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
