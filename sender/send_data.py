import requests
import logging


def send_data(api_url, token, id, values):
    """Отправляет данные через POST-запрос по заданному URL.
    В теле запроса отправляются сгенерированные значения в поле 'macros_random_values'."""

    values_str = '\n'.join(values)

    url = api_url.format(id=id, token=token)
    payload = {
        "macros_random_values": values_str
    }

    logging.info(f"Отправляемое тело запроса: {payload}")

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logging.info(f"Данные успешно отправлены. Статус: {response.status_code}. Ответ: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при отправке данных: {e}")
