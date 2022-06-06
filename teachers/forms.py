# ../teachers/forms.py

from django import forms
from django_filters import FilterSet

from .models import Teacher


class TeacherBaseForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone_number',
            'group',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class TeacherCreateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        exclude = [
            # '__all__'
            'group',
        ]

    # cleaned_date
    def clean_first_name(self):
        fn = self.cleaned_data['first_name']
        return fn.title()

    def clean_last_name(self):
        ln = self.cleaned_data['last_name']
        return ln.title()

    def clean_phone_number(self):
        phone_num = self.cleaned_data['phone_number']
        try:
            if phone_num.isnumeric():
                return phone_num
            else:
                s = ''
                for i in phone_num:
                    if i.isdigit():
                        s = s + i
                return s
        except AttributeError:
            return None


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        exclude = []
        #     'first_name',
        #     'last_name',
        #     'birthday',
        #     'phone_number',
        #     'group'
        # ]


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
