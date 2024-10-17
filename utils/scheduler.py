import logging
from datetime import datetime
from generator.generation import generate_values
from sender.send_data import send_data


def schedule_task(api_url, token, id):
    """Используя функции выполняет генерацию и отправку api запроса"""
    logging.info(f"Начало выполнения задачи: {datetime.now()}")

    values = generate_values()
    logging.info(f"Сгенерированные значения: {values}")

    send_data(api_url, token, id, values)
