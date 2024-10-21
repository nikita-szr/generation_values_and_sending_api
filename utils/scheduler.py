import logging
from datetime import datetime
from generator.generation import generate_values
from sender.send_data import send_data


def schedule_task(api_url, token, id, number_of_values):
    """Функция для выполнения задачи: генерация значений и отправка через API."""
    logging.info(f"Начало выполнения задачи: {datetime.now()}")

    # Генерация значений
    values = generate_values(number_of_values)
    logging.info(f"Сгенерированные значения: {values}")

    # Отправка данных через API
    send_data(api_url, token, id, values)
