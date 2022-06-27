# .../courses/views.py
__all__ = [
            'UpdateCourseView',
            'ListCourseView',
            'CreateCourseView',
            'DeleteCourseView',
           ]

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

from .forms import CourseCreateForm, CourseFilterForm, CourseUpdateForm

from .models import Course
from groups.models import Group


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/cr_list.html'
    # context_object_name = 'courses_filter'
    extra_context = {'title': 'List of courses'}
    paginate_by = 5


    def get_filter(self):
        return CourseFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group_course')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses_filter'] = self.get_filter().form
        return context


    # def get_queryset(self):
    #     courses_filter = CourseFilterForm(
    #         data=self.request.GET,
    #         queryset=self.model.objects.all().select_related('group_course')
    #     )
    #
    #     return courses_filter
    #

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses')
    template_name = 'courses/cr_create.html'
    extra_context = {'title': 'Create course'}


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'identity'
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses')
    template_name = 'courses/cr_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_group'] = Group.objects.filter(course_id=self.get_object().course_id)
        return context


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    pk_url_kwarg = 'identity'
    model = Course
    success_url = reverse_lazy('courses')
    template_name = 'courses/cr_delete.html'




# Кладовка

## Импорты

# __all__ = ['get_courses',
#            'create_course',
#            'update_course',
#            'delete_course',
# 
#            ]

# from webargs.djangoparser import use_args
# from webargs.fields import Date, Int,  Str
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from groups.models import Group
# from django.urls import reverse

## Вьюхи

# class ListCourseView(ListView):
#     model = Course
#     template_name = 'courses/cr_list.html'
#     context_object_name = 'courses_filter'
#     extra_context = {'title': 'List of courses'}
#
#     def get_queryset(self):
#         courses_filter = CourseFilterForm(
#             data=self.request.GET,
#             queryset=self.model.objects.all().select_related('group_course')
#         )
#
#         return courses_filter


# @use_args(
#     {
#         'course_name': Str(required=False),  # , missing=None)
#         'number_of_courses': Int(required=False),
#         'date_of_start': Date(required=False)
#     },
#     location='query'
# )
# def get_courses(request, args):
#     if request.method == 'GET':
#         form = CourseCreateForm()
#         gr = Course.objects.all()
#         for key, value in args.items():
#             gr = gr.filter(**{key: value})  # key=value
# 
#         return render(
#             request,
#             'courses/cr_licr.html',
#             {'title': 'List of courses', 'courses': gr, 'method': "get", 'args': args, 'form': form}
#         )


# def update_course(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     if request.method == 'GET':
#         form = CourseCreateForm(instance=course)
#     else:
#         form = CourseCreateForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('courses'))
#
#     return render(
#         request, 'courses/cr_update.html',
#         {'title': 'Update course', 'form': form, 'course': course},
#     )


# def get_courses(request):
#     courses = Course.objects.all()
#     courses_filter = CourseFilterForm(data=request.GET, queryset=courses)
#     return render(
#         request,
#         'courses/cr_licr.html',
#         {'courses_filter': courses_filter, 'title': 'List of courses'}  # , 'courses': courses}
#     )
# 
# 
# def create_course(request):
#     if request.method == 'GET':
#         form = CourseCreateForm()
#     else:
#         form = CourseCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
# 
#             return HttpResponseRedirect(reverse('courses'))
# 
#     return render(
#         request,
#         'courses/cr_create.html',
#         {'title': 'Create course', 'form': form}
#     )
# 
# 
# def update_course(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     course_group = Group.objects.filter(course_id=pk)
#     if request.method == 'POST':
#         form = CourseUpdateForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('courses'))
#     else:
#         form = CourseUpdateForm(instance=course)
#     return render(
#         request, 'courses/cr_update.html',
#         {'title': 'Update course', 'form': form, 'course': course, 'course_group':course_group},
#     )
# 
# 
# def delete_course(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     if request.method == 'POST':
#         course.delete()
#         return HttpResponseRedirect(reverse('courses'))
# 
#     return render(request, 'courses/cr_delete.html', {'course': course})
