"""Тесты для раздела 'Вопросы о важном'."""

import allure
import pytest
from pages.main_page import MainPage
from data.faq_data import FAQ_TEST_DATA


@allure.feature("FAQ раздел")
class TestFAQ:

    @pytest.mark.parametrize("faq_item", FAQ_TEST_DATA, ids=[item["title"] for item in FAQ_TEST_DATA])
    @allure.title("Проверка ответа на вопрос: {faq_item[title]}")
    def test_faq_question_answer(self, driver, faq_item):
        page = MainPage(driver)
        
        with allure.step(f"Прокрутить до раздела FAQ"):
            page.go_to_faq_section()
        
        with allure.step(f"Кликнуть на вопрос: '{faq_item['question']}'"):
            page.click_faq_question(faq_item["id"])
        
        with allure.step(f"Получить ответ на вопрос"):
            actual_answer = page.get_faq_answer(faq_item["id"])
        
        with allure.step("Проверить ответ"):
            allure.dynamic.description(f"Вопрос: {faq_item['question']}")
            
            assert actual_answer, f"Ответ на вопрос '{faq_item['question']}' пустой"
            
            assert actual_answer == faq_item["expected_answer"], (
                f"Неправильный ответ на вопрос '{faq_item['question']}'\n"
                f"Ожидалось: {faq_item['expected_answer']}\n"
                f"Получено: {actual_answer}"
            )
