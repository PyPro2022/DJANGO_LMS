# .../groups/views.py

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import GroupCreateForm
from .models import Group
from students.utils import qs2html

from webargs.fields import Str, Int, Date
from webargs.djangoparser import use_args


# def get_groups(request):
#     return HttpResponse('Заготовка для get_groups')


@use_args(
    {
        'group_name': Str(required=False),  # , missing=None)
        'number_of_students': Int(required=False),
        'date_of_start': Date(required=False)
    },
    location='query'
)
def get_groups(request, args):
    gp = Group.objects.all()
    for key, value in args.items():
        gp = gp.filter(**{key: value})  # key=value

    html_form = """
            <a href = "/"> Home </a>
        <br><br>

        <form method="get">
            <label for="group_name">Group name:</label><br>
            <input type="text" id="group_name" name="group_name" placeholder="Random Group"><br>
            <label for="date_of_start">Date of start:</label><br>
            <input type="date" id="date_of_start" name="date_of_start" placeholder="2022-09-01"><br>
            <label for="number_of_students">Number of students:</label><br>
            <input type="number" id="number_of_students" name="number_of_students" placeholder="?"><br>	<br>

            <input type="submit" value="Search">
        </form> 
    """
    html = qs2html(gp)
    response = html_form + html

    return HttpResponse(response)


# def create_group(request):
#     return HttpResponse('Заготовка для create_group')


@csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    html_form = f"""
            <a href = "/"> Home </a>
        <br><br>

            <form method="post">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Create">
            </form> 
        """

    return HttpResponse(html_form)


