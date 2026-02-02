from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def get_question_locator(question_number):
        """Получить локатор вопроса по номеру (0-7)."""
        return (By.ID, f"accordion__heading-{question_number}")
    
    @staticmethod
    def get_answer_locator(question_number):
        """Получить локатор ответа по номеру (0-7)."""
        return (By.ID, f"accordion__panel-{question_number}")

    TOP_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
