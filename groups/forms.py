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
            'headman',
            'teachers'
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


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
            'start_date',
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

# Документация: значение ключевых слов для настройки поиска:
# /home/user/PycharmProjects/DJANGO/venv/lib/python3.8/site-packages/django_filters/conf.py


# Кладовка
# def clean_last_name(self):
#     ln = self.cleaned_data['last_name']
#     return ln.title()
