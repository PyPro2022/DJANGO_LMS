from django.urls import path

from .views import *  # noqa

# urlpatterns = [
#     path('', get_teachers, name='teachers'),  # noqa
#     path('generate_teachers/', generate_teachers, name='gen_teachers'),  # noqa
#     path('create/', create_teacher, name='create_teacher'),  # noqa
#     path('update/<int:pk>/', update_teacher, name='update_teacher'),  # noqa
#     path('delete/<int:pk>/', delete_teacher, name='delete_teacher'),  # noqa
# ]

urlpatterns = [
    path('', ListTeacherView.as_view(), name='teachers'),  # noqa
    path('create/', CreateTeacherView.as_view(), name='create_teacher'),  # noqa
    path('update/<int:identity>/', UpdateTeacherView.as_view(), name='update_teacher'),  # noqa
    path('delete/<int:identity>/', DeleteTeacherView.as_view(), name='delete_teacher'),  # noqa
]


# Кладовка

# urlpatterns = [
#     path('', ListStudentView.as_view(), name='students'),  # noqa
#     path('create/', CreateStudentView.as_view(), name='create_student'),  # noqa
#     path('update/<int:identity>/', UpdateStudentView.as_view(), name='update_student'),  # noqa
#     path('delete/<int:identity>/', DeleteStudentView.as_view(), name='delete_student'),  # noqa
# ]
