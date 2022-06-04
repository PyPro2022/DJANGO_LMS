# ../teachers/forms.py

from django import forms

from .models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            # '__all__'
            'first_name',
            'last_name',
            # 'age',
            'birthday',
            'phone_number'
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

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
