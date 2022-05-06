from django.db import models

# Create your models here.
class Teachers (models.Model):
    fields = {'name' : str,
              'surename' : str,
              'age' : int,
              'courses' : dict or list,
              'raiting' : float,

              'groups' : dict or list,
              'lessons':dict}
