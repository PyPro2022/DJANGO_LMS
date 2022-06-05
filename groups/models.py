# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/groups/models.py

from django.core.validators import MinLengthValidator
from django.db import models

from .validators import max_student_number_validator


# from students.models import Student
# from teachers.models import Teacher


class Group(models.Model):
    group_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='groupID'
    )
    group_name = models.CharField(
        max_length=30,
        verbose_name='group name',
        validators=[MinLengthValidator(2)]
    )
    number_of_students = models.PositiveSmallIntegerField(
        null=True,
        verbose_name='number of students',
        validators=[max_student_number_validator]
    )

    date_of_start = models.DateField(verbose_name='date of start')

    date_of_end = models.DateField(null=True, verbose_name='date of end')

    class Meta:
        db_table = 'group'


    @staticmethod
    def add_students():
        pass

    @staticmethod
    def set_teacher():
        pass

    @staticmethod
    def set_date_of_start():
        pass

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    # def __str__(self):
    #     return f'{self.group_name} {self.lst_of_stdts} {self.date_of_start} {self.grp_teacher}'

    def __str__(self):
        return f'{self.group_id}. {self.group_name}  -  {self.date_of_start}  -  {self.number_of_students}'
