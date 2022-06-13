from django.urls import path

from .views import *  # noqa

urlpatterns = [  # noqa
    path('', get_courses, name='courses'),  # noqa
    path('create/', create_course, name='create_course'),  # noqa
    path('update/<int:pk>/', update_course, name='update_course'),  # noqa
    path('delete/<int:pk>/', delete_course, name='delete_course'),  # noqa
]
