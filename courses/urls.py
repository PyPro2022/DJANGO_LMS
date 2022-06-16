from django.urls import path

from .views import *  # noqa


urlpatterns = [
    path('', ListCourseView.as_view(), name='courses'),  # noqa
    path('create/', CreateCourseView.as_view(), name='create_course'),  # noqa
    path('update/<int:identity>/', UpdateCourseView.as_view(), name='update_course'),  # noqa
    path('delete/<int:identity>/', DeleteCourseView.as_view(), name='delete_course'),  # noqa
]


# Кладовка
# urlpatterns = [  # noqa
#     path('', get_courses, name='courses'),  # noqa
#     path('create/', create_course, name='create_course'),  # noqa
#     path('update/<int:pk>/', update_course, name='update_course'),  # noqa
#     path('delete/<int:pk>/', delete_course, name='delete_course'),  # noqa
# ]
