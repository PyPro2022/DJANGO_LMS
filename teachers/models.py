# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/teachers/models.py

from django.db import models
# from groups.models import Group
from faker import Faker

class Teacher (models.Model):
    teacher_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}, {self.age} {self.wgroup}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}'


#Пусть пока полежит ))
    @staticmethod
    def gen_teachers(cnt=10):
        fk = Faker('it_IT')
        for _ in range(cnt):
            tch = Teacher(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                age=fk.random_int(min=25, max=55)
            )
            tch.save()




