# /home/user/PycharmProjects/DJANGO/DJANGO_LMS/teachers/views.py
__all__ = [
            'UpdateTeacherView',
            'ListTeacherView',
            'CreateTeacherView',
            'DeleteTeacherView',
           ]

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy  # noqa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # noqa

from .forms import TeacherCreateForm, TeacherFilterForm, TeacherUpdateForm  # noqa
from .models import Teacher  # noqa


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/th_list.html'
    context_object_name = 'teachers_filter'

    def get_queryset(self):
        teachers_filter = TeacherFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all()  # .select_related('group', 'headman_group')
        )

        return teachers_filter


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers')
    template_name = 'teachers/th_create.html'
    extra_context = {'title': 'Create teacher'}


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'identity'
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers')
    template_name = 'teachers/th_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = self.get_object().groups.all()
        return context


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    pk_url_kwarg = 'identity'
    model = Teacher
    success_url = reverse_lazy('teachers')
    template_name = 'teachers/th_delete.html'



# Кладовка

# # Импорты
# __all__ = ['generate_teachers',
#            'create_teacher',
#            'get_teachers',
#            'update_teacher',
#            'delete_teacher',
#            ]
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from webargs.djangoparser import use_args, use_kwargs  # noqa
# from webargs.fields import Int, Str   # noqa


##ВЬюхи

# def get_teachers(request):
#     teachers = Teacher.objects.all()
#     teachers_filter = TeacherFilterForm(data=request.GET, queryset=teachers)
#     return render(
#         request,
#         'teachers/th_list.html',
#         {'teachers_filter': teachers_filter}  # , 'teachers': teachers}
#     )

# def create_teacher(request):
#     if request.method == 'GET':
#         form = TeacherCreateForm()
#     else:
#         form = TeacherCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers'))
#     return render(
#         request,
#         'teachers/th_create.html',
#         {'title': 'Create teacher', 'form': form}
#     )

# def update_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, pk=pk)
#     if request.method == 'POST':
#         form = TeacherUpdateForm(request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers'))
#     else:
#         form = TeacherUpdateForm(instance=teacher)
#     return render(
#         request, 'teachers/th_update.html',
#         {'title': 'Update teacher', 'form': form, 'teacher':teacher},
#     )

# def delete_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, pk=pk)
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers'))
#
#     return render(request, 'teachers/th_delete.html', {'teacher': teacher})



# @use_args(
#     {
#         'first_name': Str(required=False),  # , missing=None)
#         'last_name': Str(required=False),
#         'age': Int(required=False)
#     },
#     location='query'
# )
# def get_teachers(request, args):
#     if request.method == 'GET':
#         form = TeacherCreateForm()
#         th = Teacher.objects.all()
#         for key, value in args.items():
#             th = th.filter(**{key: value})
# 
#         return render(
#             request,
#             'teachers/th_list.html',
#             {'title': 'List of teachers', 'teachers': th, 'method': "get", 'args': args, 'form': form}
#         )

# @use_kwargs(
#     {'cnt': Int(required=False)},
#     location='query'
# )
# def generate_teachers(request, cnt=0, max_number=100):
#     if cnt == 10:
#         Teacher.gen_teachers(cnt=0)
#         return HttpResponseRedirect(reverse('teachers'))
#     else:
#         Teacher.gen_teachers(cnt=cnt)
#         if cnt:
#             return HttpResponseRedirect(reverse('teachers'))
#     return render(
#         request,
#         'teachers/generate_teachers.html',
#         {'title': 'Generate teachers',
#          'message01': f'Input the number of teachers (max = {max_number}) you wish to generate.',
#          'message02': f'{cnt} teacher(-s) has been generated',
#          'max': max_number}  # , 'kwargs':kwargs}
#     )

