# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/courses/models.py

# import datetime
# import random
import datetime
import random

from django.core.validators import MinLengthValidator
from django.db import models

# from .validators import max_student_number_validator

# from students.models import Student
from groups.models import Group


class Course(models.Model):
    course_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        # verbose_name='course id'
    )
    name = models.CharField(
        max_length=30,
        verbose_name='course name',
        validators=[MinLengthValidator(2)],
    )

    duration = models.PositiveIntegerField(blank=True, verbose_name='course duration')
    price = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='course price')
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        db_table = 'courses'

    def __str__(self):
        return f'{self.name} - {self.duration} - {self.price}'


    @staticmethod
    def gen_course():
        lst = ['PMP', 'HTWL', 'Pi/Pi++', 'Brython', 'SMS', 'Pi#', 'Machine Burning', 'Data Silence', 'Jabba', 'ZQL']
        for _ in lst:
            cr = Course(name=_,
                       duration=random.randint(8,72),
                       price=random.randint(1000,9999),
                       #Перенести courses в модель group=
            )
            cr.save()
    
    def get_number_of_groups(self):
        # from students.models import Student
        return len(Group.objects.filter(course_id=self.course_id))


# Кладовка

# def get_number_of_students(self):
#     from students.models import Student
#     return len(Student.objects.filter(course_id=self.course_id))
#
# def get_number_of_teachers(self):
#     # from teachers.models import Teacher
#     return len(Course.objects.filter(course_id=self.course_id)[0].teachers.all())
