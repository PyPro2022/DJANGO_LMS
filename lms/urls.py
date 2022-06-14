# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/lms/urls.py

"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from students.views import *
from teachers.views import *
from groups.views import *

# from students.views import readme_md

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),

    path('students/', get_students, name = 'students'),  # Read
    path('students/create/', create_student, name = 'create_student'),
    path('students/update/<int:pk>/', update_student, name='update_student'),
    path('students/delete/<int:pk>/', delete_student, name='delete_student'),

    path('teachers/', get_teachers, name = 'teachers'),
    path('generate_teachers/', generate_teachers, name = 'gen_teachers'),
    path('teachers/create/', create_teacher, name = 'create_teacher'),
    path('teachers/update/<int:pk>/', update_teacher, name='update_teacher'),
    path('teachers/delete/<int:pk>/', delete_teacher, name='delete_teacher'),

    path('groups/', get_groups, name = 'groups'),
    path('groups/create/', create_group, name = 'create_group'),
    path('groups/update/<int:pk>/', update_group, name='update_group'),
    path('groups/delete/<int:pk>/', delete_group, name='delete_group'),

    # path('readme', readme_md, name = 'README'),



]
