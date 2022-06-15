from django.urls import path

from .views import * # noqa

urlpatterns = [
    path('', get_students, name='students'),  # noqa
    path('create/', create_student, name='create_student'),  # noqa
    # path('update/<int:pk>/', update_student, name='update_student'),  # noqa
    path('update/<int:identity>/', UpdateStudentView.as_view(), name='update_student'),  # noqa
    path('delete/<int:pk>/', delete_student, name='delete_student'),  # noqa
    path('delete/<int:pk>/', delete_student, name='delete_student'),  # noqa
    path('generate_students/', generate_students, name='gen_students'),  # noqa
]
