from django.urls import path


from .views import *



urlpatterns = [
    path('', get_students, name = 'students'),
    path('create/', create_student, name = 'create_student'),
    path('update/<int:pk>/', update_student, name='update_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
    path('generate_students/', generate_students, name='gen_students'),

]