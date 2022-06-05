# .../DJANGO_LMS/students/models.py
import random

import datetime
from dateutil.relativedelta import relativedelta

from django.db import models

from core.validators import AdultValidator
from django.core.validators import MinLengthValidator
from .validators import uniqness_validator

from faker import Faker

from .utils import normalize_phone_number

from groups.models import Group


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
        null=True,
        blank=True,
        max_length=20,
        verbose_name='phone number',
        validators=[MinLengthValidator(10), uniqness_validator]
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        db_table = 'students'

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name} - {self.age} - {self.phone_number}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @staticmethod
    def gen_students(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            st = Student(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                birthday=fk.date_between(start_date='-65y', end_date='-15y'),
                phone_number=normalize_phone_number(fk.phone_number()),
                group = random.choice(Group.objects.all())
            )
            st.save()

    @staticmethod
    def set_group():
        st = Student.objects.all()
        for i in st:
            i.group = random.choice(Group.objects.all())
            i.save()

# Кладовка: #noqa

# def save(self, *args, **kwargs): #noqa
#     self.age = relativedelta(datetime.date.today(), self.birthday).years  #noqa
#     # self.phone_number = normalize_phone_number(self.phone_number)  #noqa
#     super().save(*args, **kwargs)  #noqa
