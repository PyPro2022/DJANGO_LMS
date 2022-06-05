# .../teachers/models.py

import datetime
import random

from dateutil.relativedelta import relativedelta

from django.db import models

from groups.models import Group

from core.validators import AdultValidator
from django.core.validators import MinLengthValidator
from .validators import uniqness_validator

from faker import Faker

from .utils import normalize_phone_number



class Teacher(models.Model):
    teacher_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='teacherID'
    )
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
        validators=[AdultValidator(25)]
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
        related_name='teachers')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teachers'


    def __str__(self):
        return f'{self.teacher_id}. {self.first_name} {self.last_name} - {self.age} - {self.phone_number}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @staticmethod
    def gen_teachers(cnt=10):
        fk = Faker('it_IT')
        for _ in range(cnt):
            tch = Teacher(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                birthday=fk.date_between(start_date='-55y', end_date='-25y'),
                phone_number=normalize_phone_number(fk.phone_number()),
                group = random.choice(Group.objects.all())
            )
            tch.save()

    @staticmethod
    def set_groups():
        th = Teacher.objects.all()
        for i in th:
            i.group = random.choice(Group.objects.all())
            i.save()




# Кладовка


# def save(self, *args, **kwargs):
#     self.age = relativedelta(datetime.date.today(), self.birthday).years
#     super().save(*args, **kwargs)
#
