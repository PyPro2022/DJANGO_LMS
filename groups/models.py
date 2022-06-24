# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/groups/models.py

import datetime
import random
from dateutil.relativedelta import relativedelta

from django.db import models

from django.core.validators import MinLengthValidator
# from .validators import max_student_number_validator

from teachers.models import Teacher


class Group(models.Model):
    group_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        # verbose_name='group id'
    )

    name = models.CharField(
        max_length=30,
        verbose_name='group name',
        validators=[MinLengthValidator(2)]
    )
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    course = models.OneToOneField(
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='group_course',
        default=None
    )
    teachers = models.ManyToManyField(
        to=Teacher,
        # null=True,
        blank=True,
        related_name='groups'
    )

    start_date = models.DateField(null=True, blank=True, verbose_name='date of start')
    end_date = models.DateField(null=True, blank=True, verbose_name='date of end')
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_id}. {self.name} - {self.start_date} '

    def get_number_of_students(self):
        from students.models import Student
        return len(Student.objects.filter(group_id=self.group_id))

    def get_number_of_teachers(self):
        return len(Group.objects.filter(group_id=self.group_id)[0].teachers.all())

    @staticmethod
    def gen_group():
        lst = ['alfa', 'beta', 'gamma', 'delta', 'epsilon', 'theta', 'capa', 'lambda', 'sigma', 'omega']
        for _ in lst:
            gr = Group(name=_.capitalize(),
                       start_date=datetime.date(random.choice([i for i in range(2022,2024)]),
                                                random.choice([i for i in range(1,13)]),
                                                random.choice([i for i in range(1,30)])
                                                ))
            gr.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            dur = Group.objects.get(course_id=self.course_id).course.duration
            self.end_date = self.start_date + relativedelta(weeks=dur * 2 + random.randint(0, 5))
            super().save(*args, **kwargs)
        except AttributeError:
            self.end_date = None
            super().save(*args, **kwargs)


# Кладовка

# @staticmethod
# def add_students():
#     pass
#
# @staticmethod
# def set_teacher():
#     pass
#
# @staticmethod
# def set_date_of_start():
#     pass

# def __str__(self):
#     return f'{self.group_name} {self.lst_of_stdts} {self.date_of_start} {self.grp_teacher}'


    # number_of_students = models.PositiveSmallIntegerField(
    #     null=True,
    #     verbose_name='number of students',
    #     validators=[max_student_number_validator]
    # )



    # @staticmethod
    # def set_crt_upd_time(TIMESHIFT=0):
    #
    #     MONTH = random.choice([i for i in range(5, 7)])
    #     HOUR = random.choice([i for i in range(1, 23)])
    #     MINUTE = random.choice([i for i in range(0, 60)])
    #     SEC = random.choice([i for i in range(0, 60)])
    #     TIMESHIFT = 0
    #     DAY = {5: random.choice([i for i in range(10, 31)]),
    #            6: random.choice([i for i in range(1, 6)])}
    #
    #     if MONTH == 5:
    #         return datetime.datetime(2022, MONTH, DAY[5], HOUR + TIMESHIFT, MINUTE, SEC)
    #
    #     else:
    #         return datetime.datetime(2022, MONTH, DAY[6], HOUR + TIMESHIFT, MINUTE, SEC)
    #
    # @staticmethod
    # def set_datetime_defualts():
    #     gr = Group.objects.all()
    #     for i in gr:
    #         i.create_datetime = i.set_crt_upd_time(TIMESHIFT=0)
    #         i.update_datetime = i.set_crt_upd_time(TIMESHIFT=1)
    #         i.save()

    # @staticmethod
    # def set_headman():
    #     gr = Group.objects.all()
    #     for i in gr:
    #         i.headman = random.choice(Student.objects.all())
    #         i.save()
