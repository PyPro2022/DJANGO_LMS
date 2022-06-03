# .../DJANGO_LMS/students/views.py
__all__ = [
            'get_students',
           'create_student',
           'get_students',
           'update_student',
           'delete_student',

]

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StudentCreateForm
from .models import Student

from webargs.fields import Str, Int, Date
from webargs.djangoparser import use_args

# context = []

@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'birthday': Date(required=False),
        },
    location='query'
)
def get_students(request, args):
    if request.method == 'GET':
        form = StudentCreateForm()
        st = Student.objects.all()
        for key, value in args.items():
            st = st.filter(**{key: value})
        return render(
            request,
            'students/st_list.html',
            {'title': 'List of students', 'students': st, 'method':"get", 'args':args, 'form': form}
        )



def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students'))
    return render(
        request,
        'students/st_create.html',
        {'title': 'Create student', 'form': form}
    )


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    else:
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students'))

    return render(
        request, 'students/st_update.html',
        {'title': 'Update student', 'form': form},
    )




def delete_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students'))

    return render(request, 'students/st_delete.html', {'student': student})







# попытка реализовть вывод содержимого _README.md на главную страницу LMS. Пусть пока полежит.
# def readme_md(request):
#     return render(request, 'README.html')

