from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
import re

class MinLengthValidator(BaseValidator):
    def __init__(self, limit_value):
        # Передаем ограничение (limit_value) в родительский класс
        super().__init__(limit_value)

    def compare(self, value, limit_value):
        # Преобразуем значение в строку и проверяем длину
        return len(str(value)) < limit_value

    def clean(self, value):
        # Преобразуем значение в строку перед сравнением
        return str(value)


def validate_latin_characters(value):
    if not re.match(r'^[a-zA-Z]+$', value):
        raise ValidationError('Это поле должно содержать только латинские буквы.')
