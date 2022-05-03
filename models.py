from django.db import models

#Схема будущих моделей
class Teachers (models.Model):
    fields = {'name' : str,
              'surename' : str,
              'age' : int,
              'courses' : dict or list,
              'raiting' : float,
              'groups' : dict or list,
              'lessons':dict}




class Groups (models.Model):

    fields = {'group_name': str,
              'courses': list,
              'lst_of_stdts': dict or list,
              'grades': dict or list
              }