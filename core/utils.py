# .../DJANGO_LMS/students/utils.py

def qs2html(qs):
    lst = []
    if qs is not None:
        for line in qs:
            lst.append(str(line))
    else:
        lst.append('QuerySet is empty')

    return '<br>'.join(lst)


# Первый вариант валидатора. Пусть пока полежит.
def normalize_phone_number(phone_num):
    try:
        if phone_num.isnumeric():
            return phone_num
        else:
            s = ''
            for i in phone_num:
                if i.isdigit():
                    s = s + i
            return s
    except AttributeError:
        return None
