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

from students.views import create_student, index
from students.views import get_students, create_student #, update_student



from teachers.views import generate_teachers, create_teacher, get_teachers

from groups.views import get_groups, create_group

# from students.views import readme_md

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),

    path('students/', get_students, name = 'students'),  # Read
    path('students/create/', create_student, name = 'create_student'),
    # path('students/update/', update_student, name='update_student'),

    path('teachers/', get_teachers, name = 'teachers'),
    path('generate_teachers/', generate_teachers, name = 'gen_teachers'),
    path('teachers/create/', create_teacher, name = 'create_teacher'),

    path('groups/', get_groups, name = 'groups'),
    path('groups/create/', create_group, name = 'create_group')

    # path('readme', readme_md, name = 'README'),



]
