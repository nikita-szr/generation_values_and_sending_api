import json
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from utils.logger import setup_logging
from utils.scheduler import schedule_task

# Конфигурация из файла
def load_config(config_path='config.json'):
    with open(config_path) as f:
        return json.load(f)

# Основная функция
def main():
    # Логирование
    setup_logging()

    # Загрузка конфигурации
    config = load_config()
    api_url = config['api_url']
    token = config['token']
    ids = config['ids']  # Три ID
    number_of_values = config['number_of_values']  # Количество значений для генерации

    # Планировщик
    scheduler = BlockingScheduler()

    # Настройка расписания выполнения задачи
    scheduler.add_job(schedule_task, 'interval', weeks=1,
                      args=[api_url, token, ids, number_of_values],
                      next_run_time=config['next_run_time'])

    logging.info("Скрипт запущен и ждёт выполнения.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Скрипт остановлен.")

if __name__ == "__main__":
    main()
