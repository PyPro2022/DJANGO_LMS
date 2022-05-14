# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/groups/models.py

from django.db import models
# from students.models import Student
# from teachers.models import Teacher


class Group (models.Model):

    group_id = models.BigAutoField(primary_key = True)
    group_name = models.CharField(max_length=100)
    date_of_start = models.DateField()

    @staticmethod
    def add_students():
        pass

    @staticmethod
    def set_teacher():
        pass

    @staticmethod
    def set_date_of_start():
        pass

    # def __str__(self):
    #     return f'{self.group_name} {self.lst_of_stdts} {self.date_of_start} {self.grp_teacher}'

    def __str__(self):
        return f'{self.group_id} {self.group_name} {self.date_of_start}'



