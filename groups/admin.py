# .../DJANGO_LMS/groups/admin.py
from django.contrib import admin

from groups.models import Group
from students.models import Student

# from teachers.models import Teacher


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
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

# Подумать

# class TeachersInlineTable(admin.TabularInline):
#     model = Teacher
#     related_name = 'groups'
#     fields = [
#         'first_name',
#         'last_name',
#         'birthday',
#         'phone_number',
#     ]
#
#     extra = 0
#     readonly_fields = fields
#     # [
#     #     'first_name',
#     #     'last_name',
#     # ]
#     # show_change_link = True
#     #
#
#     def teachers(self, instance):
#         return instance.objects.teachers.all()
#
#     def has_add_permission(self, request, obj):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start_date',
        'end_date',
        'headman'
    ]

    fields = [
        'name',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
        ('create_datetime', 'update_datetime')
    ]

    readonly_fields = ['create_datetime', 'update_datetime']

    inlines = [StudentsInlineTable]  #, TeachersInlineTable]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        return form


admin.site.register(Group, GroupAdmin)