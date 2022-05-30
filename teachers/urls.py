from django.urls import path


from .views import *



urlpatterns = [
    path('', get_teachers, name = 'teachers'),
    path('generate_teachers/', generate_teachers, name = 'gen_teachers'),
    path('create/', create_teacher, name = 'create_teacher'),
    path('update/<int:pk>/', update_teacher, name='update_teacher'),
    path('delete/<int:pk>/', delete_teacher, name='delete_teacher'),
]
