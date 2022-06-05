# ../groups/forms.py

from django import forms

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'group_name',
            'number_of_students',
            'date_of_start',
            'date_of_end',

        ]

        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'}),
            'date_of_end': forms.DateInput(attrs={'type': 'date'})
        }

    # cleaned_data
    def clean_group_name(self):
        gn = self.cleaned_data['group_name']
        return gn.title()

    # def clean_last_name(self):
    #     ln = self.cleaned_data['last_name']
    #     return ln.title()
