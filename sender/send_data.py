import requests
import logging


def send_data(api_url, token, id, values):
    """Отправляет данные через метод POST по заданному URL.
    В теле запроса отправляются сгенерированные значения в поле "macros_random_values" """
    url = api_url.format(id=id, token=token)
    payload = {
        "macros_random_values": values
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logging.info(f"Данные успешно отправлены. Статус: {response.status_code}. Ответ: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при отправке данных: {e}")
