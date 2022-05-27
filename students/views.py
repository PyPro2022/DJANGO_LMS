# .../DJANGO_LMS/students/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import StudentCreateForm
from .models import Student
from .utils import qs2html

from webargs.fields import Str, Int
from webargs.djangoparser import use_args

# context = []

def index(request):
    return render(request, 'index.html')


@use_args(
    {
        'first_name': Str(required=False),       # , missing=None)
        'last_name': Str(required=False),
        'age': Int(required=False),
        },
    location='query'
)
def get_students(request, args):
    st = Student.objects.all()
    for key, value in args.items():
        st = st.filter(**{key: value})      # key=value
    html_form = """
        <a href = "/"> Home </a>
        <br><br>
        <form method="get">
            <label for="fname">First name:</label><br>
            <input type="text" id="fname" name="first_name" placeholder="Bob"><br>
            <label for="lname">Last name:</label><br>
            <input type="text" id="lname" name="last_name" placeholder="Dilan"><br>
            <label for="age_id">Age:</label><br>
            <input type="number" id="age_id" name="age" placeholder="45"><br>	<br>

            <input type="submit" value="Search">
        </form>
    """
    html = qs2html(st)
    response = html_form + html

    return HttpResponse(response)
    # return render(request, 'student_list_table.html')


@csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/students/')

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


# попытка реализовть вывод содержимого _README.md на главную страницу LMS. Пусть пока полежит.
# def readme_md(request):
#     return render(request, 'README.html')
