ORDER_TEST_DATA = [
    {
        "button": "top",
        "description": "Заказ через верхнюю кнопку (минимальные данные)",
        "data": {  # ← Добавьте этот ключ
            "name": "Николай",
            "last_name": "Дмитриев",
            "address": "ул. Ленина, 1",
            "metro_station": "Сокольники",
            "phone": "+79991234567",
            "delivery_date": "15.12.2024",
            "rental_period": "сутки",
            "color": "black",
            "comment": ""
        }
    },
    {
        "button": "bottom",
        "description": "Заказ через нижнюю кнопку (полные данные)",
        "data": {  # ← Добавьте этот ключ
            "name": "Мария",
            "last_name": "Петрова",
            "address": "пр. Мира, 15, кв. 42",
            "metro_station": "Черкизовская",
            "phone": "89998765432",
            "delivery_date": "20.12.2024",
            "rental_period": "двое суток",
            "color": "grey",
            "comment": "Позвонить за 30 минут до доставки. Код домофона 123"
        }
    },
    {
        "button": "top",
        "description": "Заказ через верхнюю кнопку (альтернативные данные)",
        "data": {  # ← Добавьте этот ключ
            "name": "Алексей",
            "last_name": "Смирнов",
            "address": "ул. Тверская, 25, подъезд 3",
            "metro_station": "Чистые пруды",
            "phone": "+79161234567",
            "delivery_date": "25.12.2024",
            "rental_period": "семеро суток",
            "color": "black",
            "comment": "Оставить у консьержа"
        }
    }
]
