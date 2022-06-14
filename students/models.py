# .../DJANGO_LMS/students/models.py

import datetime
import random

from dateutil.relativedelta import relativedelta

from django.db import models

from groups.models import Group

from core.models import BaseModel


class Student(BaseModel):
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        db_table = 'students'

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name} - {self.birthday} - {self.phone_number}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.save()


# Кладовка: #noqa

# def save(self, *args, **kwargs): #noqa
#     self.age = relativedelta(datetime.date.today(), self.birthday).years  #noqa
#     # self.phone_number = normalize_phone_number(self.phone_number)  #noqa
#     super().save(*args, **kwargs)  #noqa


# from core.validators import AdultValidator
# from django.core.validators import MinLengthValidator
# from .validators import uniqness_validator
#
# from faker import Faker
#
# from .utils import normalize_phone_number


    # @staticmethod
    # def gen_students(cnt=10):
    #     fk = Faker()
    #     for _ in range(cnt):
    #         st = Student(
    #             first_name=fk.first_name(),
    #             last_name=fk.last_name(),
    #             birthday=fk.date_between(start_date='-65y', end_date='-15y'),
    #             phone_number=normalize_phone_number(fk.phone_number()),
    #             group = random.choice(Group.objects.all())
    #         )
    #         st.save()
    #
    # @staticmethod
    # def set_groups():
    #     st = Student.objects.all()
    #     for i in st:
    #         i.group = random.choice(Group.objects.all())
    #         i.save()
