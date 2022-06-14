# ../groups/forms.py

from django import forms
from django_filters import FilterSet

from .models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [     # '__all__'
            'name',
            #  'number_of_students',
            'start_date',
            'end_date',
            'course',
            'headman',
            'teachers'

        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        help_texts = {'teachers':'Use CTRL or CMD key for multiple selection'}

class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            # 'start_date',
            # 'number_of_students',
            'end_date',

        ]

    # cleaned_data
    def clean_name(self):
        gn = self.cleaned_data['name']
        return gn.title()


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'end_date',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'start_date': ['exact','year', 'month', 'day'],
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels ={'start_date':['','year', 'month', 'day']}

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
