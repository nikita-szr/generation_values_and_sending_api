import random
import string
import json
import os
from datetime import datetime, timedelta


def load_generated_values(file_path='generated_values.json'):
    """Загружает ранее сгенерированные значения из файла"""
    if os.path.exists(file_path):
        if os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                    last_generated_date = datetime.strptime(data['date'], '%Y-%m-%d')
                    if datetime.now() - last_generated_date > timedelta(weeks=1):
                        return set()
                    return set(data['values'])
                except json.JSONDecodeError:
                    return set()
        else:
            return set()
    return set()


def save_generated_values(values, file_path='generated_values.json'):
    """Сохраняет сгенерированные значения в файл вместе с текущей датой"""
    data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'values': list(values)
    }
    with open(file_path, 'w') as f:
        json.dump(data, f)


def generate_values():
    """Генерирует 10 уникальных чисел от 7 до 10 символов, избегая дубликатов за неделю"""
    generated_values = load_generated_values()
    new_values = set()

    while len(new_values) < 10:
        value = ''.join(random.choices(string.digits, k=random.randint(7, 10)))
        if value not in generated_values:
            new_values.add(value)
            generated_values.add(value)

    # Сохраняем новые значения
    save_generated_values(new_values)
    return list(new_values)
