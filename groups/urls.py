from django.urls import path

from .views import *  # noqa

urlpatterns = [  # noqa
    path('', ListGroupView.as_view(), name='groups'),  # noqa
    path('create/', CreateGroupView.as_view(), name='create_group'),  # noqa
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update_group'),  # noqa
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete_group'),  # noqa
]
