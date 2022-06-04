# .../groups/views.py

__all__ = ['get_groups',
           'create_group',
           'update_group',
           'delete_group',

           ]

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Date, Int,  Str

from .forms import GroupCreateForm
from .models import Group


@use_args(
    {
        'group_name': Str(required=False),  # , missing=None)
        'number_of_groups': Int(required=False),
        'date_of_start': Date(required=False)
    },
    location='query'
)
def get_groups(request, args):
    if request.method == 'GET':
        form = GroupCreateForm()
        gr = Group.objects.all()
        for key, value in args.items():
            gr = gr.filter(**{key: value})  # key=value

        return render(
            request,
            'groups/gr_list.html',
            {'title': 'List of groups', 'groups': gr, 'method': "get", 'args': args, 'form': form}
        )


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups'))

    return render(
        request,
        'groups/gr_create.html',
        {'title': 'Create group', 'form': form}
    )


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups'))

    return render(
        request, 'groups/gr_update.html',
        {'title': 'Update group', 'form': form},
    )


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups'))

    return render(request, 'groups/gr_delete.html', {'group': group})
