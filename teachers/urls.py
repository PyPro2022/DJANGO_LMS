from django.urls import path

from .views import *  # noqa

urlpatterns = [
    path('', get_teachers, name='teachers'),  # noqa
    path('generate_teachers/', generate_teachers, name='gen_teachers'),  # noqa
    path('create/', create_teacher, name='create_teacher'),  # noqa
    path('update/<int:pk>/', update_teacher, name='update_teacher'),  # noqa
    path('delete/<int:pk>/', delete_teacher, name='delete_teacher'),  # noqa
]
