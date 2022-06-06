# ../groups/forms.py

from django import forms
from django_filters import FilterSet

from .models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'group_name',
            # 'number_of_students',
            'date_of_start',
            'date_of_end',

        ]
        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'}),
            'date_of_end': forms.DateInput(attrs={'type': 'date'})
        }


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            # 'date_of_start',
            # 'number_of_students',
            'date_of_end',

        ]

    # cleaned_data
    def clean_group_name(self):
        gn = self.cleaned_data['group_name']
        return gn.title()


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = []
            # 'date_of_start',
            # 'number_of_students',

class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            'date_of_start': ['exact','year', 'month', 'day'],
        }
        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'}),
        }

# Документация: значение ключевых слов для настройки поиска:
# /home/user/PycharmProjects/DJANGO/venv/lib/python3.8/site-packages/django_filters/conf.py


# Кладовка
# def clean_last_name(self):
#     ln = self.cleaned_data['last_name']
#     return ln.title()
