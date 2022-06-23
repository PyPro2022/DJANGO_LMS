# .../DJANGO_LMS/students/admin.py
from django.contrib import admin  # noqa

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'group',
    ]

    list_display_links = list_display  # сделать все поля ссылками
    list_per_page = 15  # пагинация
    search_fields = [   # панель поиска
        'first_name',
        'last_name',
    ]
    list_filter = [     # фильтр
        'group',
    ]

    fields = [              # переопределили поля на форме редактирования студента
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'phone_number',
        'group',
    ]

    readonly_fields = ['age']  # нередактируемое поле

    def age(self, instance):
        return instance.get_age()

    age.short_description = 'Age of student'


admin.site.register(Student, StudentAdmin)
