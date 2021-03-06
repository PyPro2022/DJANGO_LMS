# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/teachers/views.py
__all__ = ['generate_teachers',
           'create_teacher',
           'get_teachers',
           'update_teacher',
           'delete_teacher',

]



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import TeacherCreateForm
from .models import Teacher

from webargs.fields import Str, Int
from webargs.djangoparser import use_args, use_kwargs


@use_kwargs(
    {'cnt': Int(required=False)},
    location='query'
)
def generate_teachers(request, cnt=0, max_number=100):
        if cnt == 10:
            Teacher.gen_teachers()
        else:
            Teacher.gen_teachers(cnt=cnt)
            # return HttpResponseRedirect(reverse('teachers'))

        return render(
            request,
            'teachers/generate_teachers.html',
            {'title': 'Generate teachers',
            'message01': f'Input the number of teachers (max = {max_number}) you wish to generate.',
             'message02': f'{cnt} teacher(-s) has been generated',
             'max':max_number}#, 'kwargs':kwargs}
        )



@use_args(
    {
        'first_name': Str(required=False),  # , missing=None)
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query'
)
def get_teachers(request, args):
    th = Teacher.objects.all()
    for key, value in args.items():
        th = th.filter(**{key: value})  # key=value

    return render(
        request,
        'teachers/th_list.html',
        {'title': 'List of teachers', 'teachers': th, 'method':"get", 'args':args}
    )



def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers'))

    return render(
        request,
        'teachers/th_create.html',
        {'title': 'Create teacher', 'form': form}
    )


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers'))

    return render(
        request, 'teachers/th_update.html',
        {'title': 'Update teacher', 'form': form},
    )



def delete_teacher(request, pk):

    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers'))

    return render(request, 'teachers/th_delete.html', {'teacher': teacher})
