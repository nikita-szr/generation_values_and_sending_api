import random
import string


def generate_values():
    """Генерирует 10 случайных чисел от 7 до 10 символов """
    values = set()
    while len(values) < 10:
        value = ''.join(random.choices(string.digits, k=random.randint(7, 10)))
        values.add(value)
    return '\n'.join(values)
