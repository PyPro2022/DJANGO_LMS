# .../teachers/models.py

import datetime
import random

from dateutil.relativedelta import relativedelta

from django.db import models

from core.models import BaseModel


class Teacher(BaseModel):
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        db_table = 'teachers'

    salary = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name} - {self.phone_number}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        obj = super()._generate(locale='it_IT')
        obj.salary = random.randint(10000, 99999)
        obj.save()



# Кладовка

# from groups.models import Group
#
# from core.validators import AdultValidator
# from django.core.validators import MinLengthValidator
# from .validators import uniqness_validator
#
# from faker import Faker
#
# from .utils import normalize_phone_number


# def save(self, *args, **kwargs):
#     self.age = relativedelta(datetime.date.today(), self.birthday).years
#     super().save(*args, **kwargs)
#

    # @staticmethod
    # def gen_teachers(cnt=10):
    #     fk = Faker('it_IT')
    #     for _ in range(cnt):
    #         tch = Teacher(
    #             first_name=fk.first_name(),
    #             last_name=fk.last_name(),
    #             birthday=fk.date_between(start_date='-55y', end_date='-25y'),
    #             phone_number=normalize_phone_number(fk.phone_number()),
    #             group=random.choice(Group.objects.all())
    #         )
    #         tch.save()
    #
    # @staticmethod
    # def set_groups():
    #     th = Teacher.objects.all()
    #     for i in th:
    #         i.group = random.choice(Group.objects.all())
    #         i.save()
    #
