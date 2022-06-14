# .../groups/validators.py

import datetime

from django.core.exceptions import ValidationError


STUDENTS_LIMIT = 21
#можно реализовать в виде класса
def max_student_number_validator(number_of_students):

    if number_of_students > STUDENTS_LIMIT:
        raise ValidationError(f'Group can not contain more than {STUDENTS_LIMIT} students!')