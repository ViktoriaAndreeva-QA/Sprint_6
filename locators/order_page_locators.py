from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    
    @staticmethod
    def metro_station(station_name):
        """Локатор для станции метро по названию."""
        return (By.XPATH, f"//div[text()='{station_name}']")
    
    @staticmethod
    def rental_period(period):
        """Локатор для срока аренды."""
        return (By.XPATH, f"//div[text()='{period}']")
    
    @staticmethod
    def color_checkbox(color):
        """Локатор для цвета самоката."""
        return (By.ID, color)
    
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    CALENDAR = (By.CLASS_NAME, "react-datepicker")  # Класс календаря
    CALENDAR_MONTH = (By.CLASS_NAME, "react-datepicker__current-month")

    @staticmethod  
    def calendar_day(day_text):
        """Локатор для дня календаря по тексту."""
        return (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day_text}' and not(contains(@class, 'disabled'))]")
    
    @staticmethod
    def calendar_today():
        """Локатор для сегодняшней даты."""
        return (By.CLASS_NAME, "react-datepicker__day--today")
    
    @staticmethod
    def calendar_day_active():
        """Локатор для любого активного (не заблокированного) дня."""
        return (By.XPATH, ".//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'disabled'))]")
