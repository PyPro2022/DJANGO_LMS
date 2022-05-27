# .../teachers/validators.py

import datetime

from django.core.exceptions import ValidationError


ADULT_AGE_LIMIT = 25


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError(f'Age should be greater than {ADULT_AGE_LIMIT} y.o.')

#можно реализовать в виде класса
def uniqness_validator(new_phone_number):
    from .models import Teacher
    th = Teacher.objects.filter(phone_number=new_phone_number).exists()
    if th:
        raise ValidationError(f'This phone number is not unique! Enter other phone number')