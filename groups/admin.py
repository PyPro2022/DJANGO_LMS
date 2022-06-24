# .../DJANGO_LMS/groups/admin.py
from django.contrib import admin

from groups.models import Group
from students.models import Student


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

    # show_change_link = True  # вкл/выкл возможность редактировать поле в таблице

    def has_add_permission(self, request, obj):  # вкл/выкл возможность добавить новую запись в таблице
        return False

    def has_delete_permission(self, request, obj=None):  # вкл/выкл возможность удалить запись в таблице
        return False


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = [
        'first_name',
        'last_name',
        'age',
        'phone_number',
        'salary'
    ]
    readonly_fields = fields
    extra = 0
    # show_change_link = True

    # Наверно всё это можно было реализовать красиво через какой-нибудь classmethod, но времени в обрез,
    # поэтому вот так
    def birthday(self, instance):
        return instance.teacher.birthday

    def age(self, instance):
        return instance.teacher.get_age()

    def first_name(self, instance):
        return instance.teacher.first_name

    def last_name(self, instance):
        return instance.teacher.last_name

    def salary(self, instance):
        return instance.teacher.salary

    def phone_number(self, instance):
        return instance.teacher.phone_number

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'course',
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

    inlines = [StudentsInlineTable, TeachersInlineTable]

    # exclude = ['teachers',]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        return form


admin.site.register(Group, GroupAdmin)


#  Кладовка

# def get_params(self,instance):
#     # return dir(instance)
#     return list(instance.teacher.__dict__.keys())

# def pk(self, instance):
#     return instance.pk
#
#
# def teachers(self, instance):
#     # return dir(instance.teacher)
#     return instance.teacher.first_name + ' ' + instance.teacher.last_name

