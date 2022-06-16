# ../Courses/forms.py

from django import forms
from django_filters import FilterSet

from .models import Course


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [     # '__all__'
            'name',
            'duration',
            'price',
        ]

        # widgets = {
        #     'start_date': forms.DateInput(attrs={'type': 'date'}),
        #     'end_date': forms.DateInput(attrs={'type': 'date'}),
        # }
        help_texts = {'duration':'Number of lessons'}


class CourseCreateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        exclude = [
        ]

    # cleaned_data
    def clean_name(self):
        gn = self.cleaned_data['name']
        return gn.title()


class CourseUpdateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        exclude = [
            'name',
        ]


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains'],
            # 'start_date': ['exact','year', 'month', 'day'],
        }
        # widgets = {
        #     'start_date': forms.DateInput(attrs={'type': 'date'}),
        # }
        # labels ={'start_date':['','year', 'month', 'day']}

# Документация: значение ключевых слов для настройки поиска:
# /home/user/PycharmProjects/DJANGO/venv/lib/python3.8/site-packages/django_filters/conf.py

# Документация: атрибуты полей формы
# /home/user/PycharmProjects/DJANGO/venv/lib/python3.8/site-packages/django/forms/models.py
# django.forms.models.modelform_factory

# Документация: настройка виджетов
# /home/user/PycharmProjects/DJANGO/venv/lib/python3.8/site-packages/django/forms/widgets.py
# django.forms.widgets.ChoiceWidget

# Кладовка
# def clean_last_name(self):
#     ln = self.cleaned_data['last_name']
#     return ln.title()
