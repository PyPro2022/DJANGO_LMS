# .../DJANGO_LMS/students/models.py

import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from core.validators import AdultValidator
from .validators import uniqness_validator

from .utils import normalize_phone_number


class Student(models.Model):

    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        validators=[MinLengthValidator(2)]
    )
    # age = models.PositiveIntegerField()

    birthday = models.DateField(
        default=datetime.date.today,
        verbose_name='birthday',
        validators=[AdultValidator(18)]
    )
    phone_number = models.CharField(
        null = True,
        blank = True,
        max_length=20,
        verbose_name='phone number',
        validators=[MinLengthValidator(10), uniqness_validator]
        )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name} - {self.age} - {self.phone_number}'

    def get_age (self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @staticmethod
    def gen_students(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            st = Student(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                birthday=fk.date_between(start_date='-65y', end_date='-15y'),
                phone_number=normalize_phone_number(fk.phone_number())

            )

            st.save()

    # def save(self, *args, **kwargs):
    #     self.age = relativedelta(datetime.date.today(), self.birthday).years
    #     # self.phone_number = normalize_phone_number(self.phone_number)
    #     super().save(*args, **kwargs)

