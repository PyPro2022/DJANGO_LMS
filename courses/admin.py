from django.contrib import admin

from courses.models import Course

# from groups.admin import GroupAdmin


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'duration',
        'price',
        'group_course'
            ]

    fields = [
        ('name', 'duration', 'price'),
        ('create_datetime', 'update_datetime')
    ]

    readonly_fields = ['create_datetime', 'update_datetime']

    # inlines = [GroupAdmin]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['headman'].widget.can_add_related = False
    #     return form


admin.site.register(Course, CourseAdmin)


# Кладовка
