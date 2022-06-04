from django.urls import path

from .views import *  # noqa

urlpatterns = [  # noqa
    path('', get_groups, name='groups'),  # noqa
    path('create/', create_group, name='create_group'),  # noqa
    path('update/<int:pk>/', update_group, name='update_group'),  # noqa
    path('delete/<int:pk>/', delete_group, name='delete_group'),  # noqa
]
