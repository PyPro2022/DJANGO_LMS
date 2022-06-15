# .../groups/views.py
__all__ = [
            'UpdateGroupView',
            'ListGroupView',
            'CreateGroupView',
            'DeleteGroupView',
           ]

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import GroupCreateForm, GroupFilterForm, GroupUpdateForm
from .models import Group
from students.models import Student


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/gr_list.html'
    context_object_name = 'groups_filter'

    def get_queryset(self):
        groups_filter = GroupFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('course', 'headman')
        )

        return groups_filter



class CreateGroupView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups')
    template_name = 'groups/gr_create.html'


class UpdateGroupView(UpdateView):
    model = Group
    success_url = reverse_lazy('groups')
    form_class = GroupUpdateForm
    template_name = 'groups/gr_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            form.instance.headman = Student.objects.get(pk=form.cleaned_data['headman_field'])
            form.instance.save()
        except ValueError:
            pass

        return response


class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups')
    template_name = 'groups/gr_delete.html'




# Кладовка

##Импорты

# __all__ = ['get_groups',
#            'create_group',
#            'update_group',
#            'delete_group',
#
#            ]

# from webargs.djangoparser import use_args
# from webargs.fields import Date, Int,  Str


##Вьюхи
# def get_groups(request):
#     groups = Group.objects.all()
#     groups_filter = GroupFilterForm(data=request.GET, queryset=groups)
#     return render(
#         request,
#         'groups/gr_list.html',
#         {'groups_filter': groups_filter, 'title': 'List of groups'}  # , 'groups': groups}
#     )

# def create_group(request):
#     if request.method == 'GET':
#         form = GroupCreateForm()
#     else:
#         form = GroupCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('groups'))
#
#     return render(
#         request,
#         'groups/gr_create.html',
#         {'title': 'Create group', 'form': form}
#     )

# def update_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'POST':
#         form = GroupUpdateForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups'))
#     else:
#         form = GroupUpdateForm(instance=group)
#     return render(
#         request, 'groups/gr_update.html',
#         {'title': 'Update group', 'form': form, 'group': group},
#     )

# def delete_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#
#     if request.method == 'POST':
#         group.delete()
#         return HttpResponseRedirect(reverse('groups'))
#
#     return render(request, 'groups/gr_delete.html', {'group': group})


# @use_args(
#     {
#         'group_name': Str(required=False),  # , missing=None)
#         'number_of_groups': Int(required=False),
#         'date_of_start': Date(required=False)
#     },
#     location='query'
# )
# def get_groups(request, args):
#     if request.method == 'GET':
#         form = GroupCreateForm()
#         gr = Group.objects.all()
#         for key, value in args.items():
#             gr = gr.filter(**{key: value})  # key=value
# 
#         return render(
#             request,
#             'groups/gr_list.html',
#             {'title': 'List of groups', 'groups': gr, 'method': "get", 'args': args, 'form': form}
#         )


# def update_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     if request.method == 'GET':
#         form = GroupCreateForm(instance=group)
#     else:
#         form = GroupCreateForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('groups'))
#
#     return render(
#         request, 'groups/gr_update.html',
#         {'title': 'Update group', 'form': form, 'group': group},
#     )
