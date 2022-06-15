from django.urls import path

from .views import * # noqa

urlpatterns = [
    path('', ListStudentView.as_view(), name='students'),  # noqa
    path('create/', CreateStudentView.as_view(), name='create_student'),  # noqa
    path('update/<int:identity>/', UpdateStudentView.as_view(), name='update_student'),  # noqa
    path('delete/<int:identity>/', DeleteStudentView.as_view(), name='delete_student'),  # noqa
]
