# .../DJANGO_LMS/teachers/admin.py
from django.contrib import admin  # noqa

from teachers.models import Teacher
from groups.models import Group


class GroupsInlineTable(admin.TabularInline):
    model = Group
    fields = [
        'name',
        'course',
        'start_date',
        'end_date',
    ]

    extra = 0   # сколько доп. пустых полей будет внизу таблицы
    readonly_fields = fields
    # [
    #     'first_name',
    #     'last_name',
    # ]
    # show_change_link = True  # вкл/выкл возможность редактировать поле в таблице
    #

    def has_add_permission(self, request, obj):  # вкл/выкл возможность добавить новую запись в таблице
        return False

    def has_delete_permission(self, request, obj=None):  # вкл/выкл возможность удалить запись в таблице
        return False


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'salary',
    ]

    list_display_links = list_display  # сделать все поля ссылками
    list_per_page = 5  # пагинация
    search_fields = [   # панель поиска
        'first_name',
        'last_name',
    ]
    # list_filter = [     # фильтр
    #     'group',
    # ]

    fields = [              # переопределили поля на форме редактирования студента
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'phone_number',
        'salary',
    ]

    readonly_fields = ['age']  # нередактируемое поле

    # inlines = [GroupsInlineTable]

    def age(self, instance):
        return instance.get_age()

    age.short_description = 'Age of teacher'




admin.site.register(Teacher, TeacherAdmin)
