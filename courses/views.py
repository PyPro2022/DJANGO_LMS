# .../courses/views.py

__all__ = ['get_courses',
           'create_course',
           'update_course',
           'delete_course',

           ]

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CourseCreateForm, CourseFilterForm, CourseUpdateForm
from .models import Course
from groups.models import Group


def get_courses(request):
    courses = Course.objects.all()
    courses_filter = CourseFilterForm(data=request.GET, queryset=courses)
    return render(
        request,
        'courses/cr_list.html',
        {'courses_filter': courses_filter, 'title': 'List of courses'}  # , 'courses': courses}
    )


def create_course(request):
    if request.method == 'GET':
        form = CourseCreateForm()
    else:
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses'))

    return render(
        request,
        'courses/cr_create.html',
        {'title': 'Create course', 'form': form}
    )


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course_group = Group.objects.filter(course_id=pk)
    if request.method == 'POST':
        form = CourseUpdateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses'))
    else:
        form = CourseUpdateForm(instance=course)
    return render(
        request, 'courses/cr_update.html',
        {'title': 'Update course', 'form': form, 'course': course, 'course_group':course_group},
    )


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses'))

    return render(request, 'courses/cr_delete.html', {'course': course})

# Кладовка

# from webargs.djangoparser import use_args
# from webargs.fields import Date, Int,  Str


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
#             'courses/cr_list.html',
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
