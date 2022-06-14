from django.urls import path


from .views import *



urlpatterns = [
    path('', get_groups, name='groups'),
    path('create/', create_group, name='create_group'),
    path('update/<int:pk>/', update_group, name='update_group'),
    path('delete/<int:pk>/', delete_group, name='delete_group'),
]