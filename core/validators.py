# .../DJANGO_LMS/core/validators.py

import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ADULT_AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')


@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        age = datetime.date.today().year - args[0].year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')


def uniqness_validator(new_phone_number):
    from core.models import BaseModel
    result = BaseModel.objects.filter(phone_number=new_phone_number).exists()
    if result:
        raise ValidationError('This phone number is not unique! Enter other phone number')
