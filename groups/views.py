# .../groups/views.py

__all__ = ['get_groups',
           'create_group',
           'get_groups',
           'update_group',
           'delete_group',

]


from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import GroupCreateForm
from .models import Group

from webargs.fields import Str, Int, Date
from webargs.djangoparser import use_args

from django.urls import reverse



@use_args(
    {
        'group_name': Str(required=False),  # , missing=None)
        'number_of_groups': Int(required=False),
        'date_of_start': Date(required=False)
    },
    location='query'
)
def get_groups(request, args):
    gr = Group.objects.all()
    for key, value in args.items():
        gr = gr.filter(**{key: value})  # key=value

    return render(
        request,
        'groups/gr_list.html',
        {'title': 'List of groups', 'groups': gr, 'method':"get", 'args':args}
    )

@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    return render(
        request,
        'groups/gr_create.html',
        {'title': 'Create group', 'form': form}
    )


@csrf_exempt
def update_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

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
