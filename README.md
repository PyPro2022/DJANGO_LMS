#DJANGO_LMS learning project

Group:
    Hillel python advanced 15032022 

Student:
    Кардашев Константин
-------------------------------------
Предполагаемая структура БД
-------------------------------------
За основу взята учебная БД из Dbeaver. 
Аналогии следующие:

    Student <=> Track
    Teacher <=> Author
    Group <=> Album

Расшифровка обозначений:

        --добавленные поля---| | ---поля будут добавлены по мере разработки---


Student:

      PKey                                                      FKey, OneToOneField
    student_id -- first_name -- last_name---birthday ----phone_number --group_id--  



Teacher:

        PKey                                                       FKey, ManyToManyField
    teacher_id -- first_name -- last_name---birthday -----phone_number -- group_id


Group:

PKey                                                   FKey, ManyToManyField  FKey, OneToOneField     FKey, OneToOneField                               
group_id -- group_name -- date_of_start ---date_of_end--------teacher_id ---------headman-------------course_id--------create_datetime ----update_datetime


Course:
        PKey
    course_id----name------duration------price-----create_datetime ----update_datetime

-----------------------------------------------------------------------------------------------------------------------
ДЗ 16. Внешние ключи (DZ16_ForeignKeys)
-----------------------------------------------------------------------------------------------------------------------

###СДЕЛАНО

[x] - Установил и настроил джанго тулбар.

[x] - Оптимизировал sql запросы учителям и студентам

[x] - Добавил старосту в модель группы. Поправил формы для групп. Поправил index.html.

[x] - Добавил старосту в шаблоны групп и студентов. Поправил шаблоны.

[x] - Добавил оптимизацию sqlзапроса по старосте во вью студентов 

[x] - Добавил базовую модель в core. "Разнёс" по студенам и учителям. Поправил валидаторы.

[x] - Пересоздал базу и нагенерировал данные.

[x] - Добавил unique=true в поле телефона в базовой модели. сделал миграции

[x] - Добавил help_text на update-форму группе. Поправил вью списка учителей.

[x] - Реализовал в группах подсчёт количества студентов и учителей "на лету"

[x] - Создал приложение courses

[x] - Поправил шаблоны списков у всех моделей + шаблон меню

[x] - Создал вью для курсов. Добавил курсы в menu.html. Прописал маршруты.

[x] - Добавил курсы в модель и форму групп. Сделал миграции.

[x] - Создал и подключил формы для курсов

[x] - Создал и подключил шаблоны на все CRUD операции для курсов

[x] - Добавил вывод инфы по редактируемому объекту в update-шаблонах групп и курсов. Поправил list-шаблоны

[x] - Добавил вывод описания группы в update-шаблон для курса

[x] - Добавил автовычисление end_date при зачислении группы на курс. Поправил формы группам.

[x] - Прибрал мусор


#Можно сделать

- Валидаторы на макс. число студентов и учителей в группах

- Вылидаторы на макс зарплату учителей

- Выбор старосты через чекбокс в таблице группы

- Механизм удаления группы с курса, студента(учителя) из группы

- Механизм вычисления end_date у групп через триггер в БД.

---------------------------------------------------------------------------------------------------
ДЗ 15. Связи между таблицами (DZ15_Table_Relations)
---------------------------------------------------------------------------------------------------
###СДЕЛАНО

[x] - Подключил django-filter студентам

[x] - Добавил accordion в шаблон студентов

[x] - Поправил модель группы и студента. Сделал миграции

[x] - Поправил модель учителя. Сделал миграции

[x] - Добавил поле Groups в шаблон студентов. Написал метод автоназначения группы студенту.

[x] - Добавил Groups учителям. Автоназначил группы учителям. Поправил шаблон.

[x] - Поправил модель группы. Добавил вычисление кол-ва студентов в группе на ходу.

[x] - Разделил шаблоны list у студентов и групп. Подключил accordion.

[x] - Изменил формы группам. Добавил фильтр

[x] - Добавил accordion группам. Поменял тип и число полей.

[x] - Поправил accordion и gr_list.html

[x] - Создал st_list_table.html. Поправил вью и шаблон update для групп

[x] - Поправил формы, модели и вью у студентов. Поправил модель у групп

[x] - Поправил формы, модели и вью у учителей

[x] - Разделил шаблоны list у всех приложений

[x] - Сделал вывод учителей и студентов при обновлении группы. Поправил шаблоны list_table для всех моделей.

[x] - Добавил create_datetime и update_datetime в модель группы. Нагенерил данных в базу


---------------------------------------------------------------------------------------------------
ДЗ 14. Оформление страниц (DZ14_Pages_Design)
---------------------------------------------------------------------------------------------------
###СДЕЛАНО

[x] - Создал .env и переписал переменные окружения

[x] - Убрал age в модели студента. Поменял шаблон

[x] - Убрал age в модели учителя. Поменял шаблон

[x] - Поправил bootstrap классы в menu.html. Добавил групп в базу.

[x] - Новые стили таблиц для студентов. Убрал age, добавил birthday на форме поиска для студентов

[x] - Поменял формат даты для студентов // для всех, они ж в settings задаются ))

[x] - Подключил бутстрап. Прописал settings

[x] - Добавил crispyforms студентам. Поправил вью и шаблон

[x] - Добавил crispy forms и bs стили во все шаблоны студентов

[x] - Поправил шаблоны учителей. Поправил вью generate_teachers.

[x] - Доделал генератор учителей. Добавил генератор студентов. Добавил шаблон для генератора студентов

[x] - Подключил crispy, bs во все шаблоны групп

[x] - Добавил собственный логотип

[x] - Установил flake8 и допы. Прочесал проект // На импорты забил. У меня удобней организованы.

[x] - Поменял index 

[x] - Почистил базу. Нагенерил студентов и учителей.



---------------------------------------------------------------------------------------------------
ДЗ 13. Работа с маршрутами и шаблонами
---------------------------------------------------------------------------------------------------
[x] -templates:
    
    [x] -Заменил все хард-код пути во всех шаблонах.

    [x] - Стили подключить не удалось через спецтеги. Разбираюсь почему, поэтому пока так )) 

    [x] - Подключил generate_teachers к базовому шаблону. Поставил cnt = 0 чтобы не загаживать базу при
            каждом вызове. Отключил часть кода.

[x] -views:

    [x] - Переписал все вьюшки, кроме get_ на HttpResponseRedirect(reverse())
    
    [x] - Создал для всех моделей пременную __all__ для удобства импорта


[x] -urls:

    [x] - Разделил маршруты во всех приложениях
           
    [x] - Создал core. Почистил проект.


[x] -models:

    [x] - поменял AdultAge validator у студента и учителя

    [x] - Подправил миграции студента и учителя

    [x] - Ещё раз сделал миграции


[x] - validators: 

    [x] - Разнёс по приложениям

     
[x] - forms: 


[x] - utils: 


[x] -other:

    [x] - В предыдущей домашке забыл поменять студентов на группы в шаблоне group_list. В этой всё поправил
        
    [x] - Если что вспомню, допишу в следующем коммите в эту же ветку



---------------------------------------------------------------------------------------------------
ДЗ 12. Работа с шаблонами
---------------------------------------------------------------------------------------------------



[x] -templates:
    
    [x] -Заменил все хард код пути во всех шаблонах.

    [x] - Стили подключить не удалось через спецтеги. Разбираюсь почему, поэтому пока так )) 

    [x] - Подключил generate_teachers к базовому шаблону. Поставил cnt = 0 чтобы не загаживать базу при
            каждом вызове. Отключил часть кода.

[x] -views:

    [x] - Переписал все вьюшки, кроме get_ на HttpResponseRedirect(reverse())
    
    [x] - Создал для всех моделей пременную __all__ для удобства импорта


[x] -urls:

    [x] - Разделил маршруты во всех приложениях
           
    [x] - Создал core. Почистил проект.


[x] -models:

    [x] - поменял AdultAge validator у студента и учителя

    [x] - подправил миграции студента и учителя

    [x] - Сделал все миграции


[x] - validators: 

    [x] - исправил adult_validator в моделях студента и учителя. Теперь считает ч/з relativedelta.

     
[x] - forms: 


[x] - utils: 


[x] -other:

    [x] - В задачу не входила табличная верстка, поэтому будем считать что это не таблица, 
            а хитро организованный список )) 


---------------------------------------------------------------------------------------------------
ДЗ 11. Forms
---------------------------------------------------------------------------------------------------

[x] - validators: 

    [x] - Добавил валидаторы uniqness_validator учителю и студенту. прописал в модели.

    [x] - Добавил валидатор max_student_number_validator в группы.


     
[x] - forms: 

    [x]-  Добавил форму учителю, поправил имена полей в студентах.

    [x] - Добавил форму для групп.

    [x] - Добавил очистку для phone_number студентам и учителям

    [x] - Удалил поле age учителям и студентам
    

[x] - utils: 

    [x] - Добавил нормализатор normalize_phone_number учителю и студенту. Он нужен для генерации через faker.

[x] -models:

    [x]- Добавил в модель группы поле number_of_students

    [x]- Добавил класс Meta во все модели

    [x]- Поменял метод __str__ во всех моделях

    [x] - Во всех моделях поменял параметры полей

[x] -views:

    [x] - Создал вью для групп: get_groups, create_group

[x] -urls:

    [x] - Прописал все url всех шаблонов и вью на уровне lms

[x] -templates:

    [x] - Временно подключил шаблоны на уровне проекта для удобства контроля разработки

    [x] - Подключил шаблон README.html для вывода текущей информации по проекту
         из файла README.md. Пока через "костыль". Потом разберусь как правильно.

[x] -static:

    [x] - Подключил статику на уровне проекта. Прописал пути в settings.py


---------------------------------------------------------------------------------------------------
ДЗ 10.Models
---------------------------------------------------------------------------------------------------
1. Создан проект DJANGO_LMS.

2. Созданы приложения teachers и groups.
3. Созданы первые версии моделей teachers и groups. Осуществлены первые миграции в БД.
    По мере разработки будут добавлены ещё поля и методы. Пока поставил заглушки.
4. Создана view функция generate_teachers для генерации учителей с помощью Faker. В Faker локаль
   выбрана итальянская, чтобы было проще отличать учителей(итальянцы = бывш. римляне) и студентов(англо-саксы).
   Такое вот мнемоническое правило )). 
5. Для view функции создан простенький шаблон generate_teachers.html с формой поиска, кнопкой Generate
    и подсказками в виде простого текста на странице.
 
