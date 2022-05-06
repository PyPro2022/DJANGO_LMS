from django.db import models

# Create your models here.

class Group (models.Model):
    group_name = models.CharField(max_length=100)
    
    pass




'''
fields = {'group_name': str,
              'courses': list,
              'lst_of_stdts': dict or list,
              'grades': dict or list
              }
'''