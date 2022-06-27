# .../DJANGO_LMS/students/views.py

__all__ = [
            'UpdateStudentView',
            'ListStudentView',
            'CreateStudentView',
            'DeleteStudentView',
           ]

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import StudentCreateForm, StudentFilterForm, StudentUpdateForm
from .models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'students/st_list.html'
    paginate_by = 10

    def get_filter(self):
        return StudentFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students_filter'] = self.get_filter().form
        return context


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students')
    template_name = 'students/st_create.html'
    extra_context = {'title': 'Create student'}


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'identity'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students')
    template_name = 'students/st_update.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    pk_url_kwarg = 'identity'
    model = Student
    success_url = reverse_lazy('students')
    template_name = 'students/st_delete.html'





# Кладовка

## Импорты

# __all__ = [#'generate_students',
           # 'create_student',
           # 'get_students',
           # 'update_student',
           # 'delete_student',
    # ]

# from webargs.djangoparser import use_kwargs  # ,use_args
# from webargs.fields import Int  # ,Str, Date
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

##Вьюхи

# def get_students(request):
#     students = Student.objects.all().select_related('group', 'headman_group')
#     students_filter = StudentFilterForm(data=request.GET, queryset=students)
#     return render(
#         request,
#         'students/st_list.html',
#         {'students_filter': students_filter}  # , 'students': students}
#     )
#

# def create_student(request):
#     if request.method == 'GET':
#         form = StudentCreateForm()
#     else:
#         form = StudentCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students'))
#     return render(
#         request,
#         'students/st_create.html',
#         {'title': 'Create student', 'form': form}
#     )


# def update_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         form = StudentUpdateForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students'))
#     else:
#         form = StudentUpdateForm(instance=student)
#     return render(
#         request, 'students/st_update.html',
#         {'title': 'Update student', 'form': form, 'student':student},
#     )

# def delete_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students'))
#     return render(request, 'students/st_delete.html', {'student': student})



# @use_kwargs(
#     {'cnt': Int(required=False)},
#     location='query'
# )
# def generate_students(request, cnt=0, max_number=100):
#     if cnt == 10:
#         Student.gen_students(cnt=0)
#         return HttpResponseRedirect(reverse('students'))
#     else:
#         Student.gen_students(cnt=cnt)
#         if cnt:
#             return HttpResponseRedirect(reverse('students'))
#     return render(
#         request,
#         'students/generate_students.html',
#         {'title': 'Generate students',
#          'message01': f'Input the number of students (max = {max_number}) you wish to generate.',
#          # 'message02': f'{cnt} teacher(-s) has been generated',
#          'max': max_number}  # , 'kwargs': kwargs}
#     )
#

# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#         'birthday': Date(required=False),
#     },
#     location='query'
# )
# def get_students(request, args):
#     if request.method == 'GET':
#         form = StudentCreateForm()
#         st = Student.objects.all()
#         for key, value in args.items():
#             st = st.filter(**{key: value})
#         return render(
#             request,
#             'students/st_list.html',
#             {'title': 'List of students', 'students': st, 'method': "get", 'args': args, 'form': form}
#         )
