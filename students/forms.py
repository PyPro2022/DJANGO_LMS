# .../DJANGO_LMS/students/forms.py

from django import forms
from django_filters import FilterSet

from .models import Student


class StudentBaseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone_number',
            'group'
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class StudentCreateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
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


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        exclude = []
        #     'first_name',
        #     'last_name',
        #     'birthday',
        #     'phone_number',
        #     'group'
        # ]

class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }



