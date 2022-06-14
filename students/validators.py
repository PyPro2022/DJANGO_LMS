# .../DJANGO_LMS/students/validators.py
import datetime

from django.core.exceptions import ValidationError

ADULT_AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')

#можно реализовать в виде класса
def uniqness_validator(new_phone_number):
    from .models import Student
    st = Student.objects.filter(phone_number=new_phone_number).exists()
    if st:
        raise ValidationError(f'This phone number is not unique! Enter other phone number')