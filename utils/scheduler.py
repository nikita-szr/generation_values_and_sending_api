import logging
from datetime import datetime
from generator.generation import generate_values
from sender.send_data import send_data

def schedule_task(api_url, token, ids, number_of_values):
    """Функция для выполнения задачи: генерация значений и отправка через API по разным ID."""
    logging.info(f"Начало выполнения задачи: {datetime.now()}")

    # Генерация одного набора значений
    values = generate_values(number_of_values)
    logging.info(f"Сгенерированные значения: {values}")

    # Отправка одинаковых значений для всех указанных ID
    for id_ in ids:
        logging.info(f"Отправка данных для ID {id_}")
        send_data(api_url, token, id_, values)
