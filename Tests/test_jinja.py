from jinja2 import Template

# name = 'Сергій'
# age = 52
#
# tm = Template("Мені {{ a + 1 }} років і звуть мене  {{ n.upper() }}")
#
# msg = tm.render(n=name, a = age)
# print(msg)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# pers = Person("John", 36)
#
# tm = Template("Мені {{ p.age }} років і звуть мене  {{ p.name.upper() }}")
# msg = tm.render(p = pers)
# print(msg)


# pers = {'age': 36, 'name':'John'}
#
# # tm = Template("Мені {{ p.age }} років і звуть мене  {{ p.name.upper() }}")
# tm = Template("Мені {{ p['age'] }} років і звуть мене  {{ p['name'].upper() }}.")
# msg = tm.render(p = pers)
# print(msg)

# Екранування
# data = '''{%raw%}Модуль jinja2
# замість {{ name }}
# підставляє відповідне значення {%endraw%}'''
#
# tm = Template(data)
# msg = tm.render(name = "Петро")
# print(msg)


# Екранування спец символів(тегів) за допомогою e-escape
# (для браузера!!!, при звичайному принті цього не видно)
# Це означає, що HTML-рядок безпечний для виводу в браузері (не буде сприйматися як тег)

# link = '''В HTML-документі посилання визначаються як:
# <a href="#">Посилання<a/>'''
#
# tm = Template("{{ link | e}}")
# msg = tm.render(link = link)
# print(msg)
# Було:
# В HTML-документі посилання визначаються як: <a href="#">Посилання<a/>
# В браузері це виглядає так:
# В HTML-документі посилання визначаються як: Посилання (тобто саме як посилання)

# Стало:
# В HTML-документі посилання визначаються як:
# &lt;a href=&#34;#&#34;&gt;Посилання&lt;a/&gt;
# В браузері це тепер виглядає так:
# В HTML-документі посилання визначаються як: <a href="#">Посилання<a/> (тобто як початковий текст, а не посилання)

# Також це можна зробити по іншому:
# from jinja2 import escape         # У нових версіях Jinja2 (3.x і вище) функцію escape видалили з основного модуля jinja2.
# Функцію escape перенесли у підмодуль jinja2.utils
# from jinja2.utils import escape     # У нових версіях Jinja2 (3.1+) функцію escape повністю прибрали із модуля jinja2.utils.
# Її винесли в окремий пакет markupsafe, який Jinja2 використовує “під капотом” для безпечного екранування HTML.
# from markupsafe import escape
#
# link = '''В HTML-документі посилання визначаються як:
# <a href="#">Посилання<a/>'''
#
# msg = escape(link)
# print(msg)


# Блок for
# cities = [{'id':1, 'city':'Kiyv'},
#           {'id':2, 'city':'Harkiv'},
#           {'id':3, 'city':'Donetsk'},
#           {'id':4, 'city':'Lviv'}]
#
# link = '''<select name = "cities">
# {% for c in cities -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% endfor -%}
# <select/>
# ''' # Мінуси використовуємо, щоб убрати перенос рядка (він неявно заданий)
#
# tmpl = Template(link)
# msg = tmpl.render(cities=cities)
# print(msg)


# Блок if
# cities = [{'id':1, 'city':'Kiyv'},
#           {'id':2, 'city':'Harkiv'},
#           {'id':3, 'city':'Donetsk'},
#           {'id':4, 'city':'Lviv'}]
#
# link = '''<select name = "cities">
# {% for c in cities -%}
# {% if c.id > 2 -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% elif c.city == 'Harkiv' -%}
#     <option>{{c['city']}}</option>
# {% else -%}
#     {{c['city']}}
# {% endif -%}
# {% endfor -%}
# <select/>
# '''
#
# tmpl = Template(link)
# msg = tmpl.render(cities=cities)
# print(msg)


# Фільтри:
# sum - сума колекції
cars = [{'model': 'Toyota', 'price': 20000},
        {'model': 'Audi', 'price': 30000},
        {'model': 'Volvo', 'price': 35000},
        {'model': 'Libra', 'price': 40000},
        {'model': 'Ford', 'price': 20000}]
#
# sum(iterable, attribute=None, start=0)
# tpl = "Сумарна ціна автомобілів: {{ cs | sum(attribute = 'price') }}"
# tmpl = Template(tpl)
# msg = tmpl.render(cs=cars)
# print(msg)

digs = [1,3,5,7,8,2]
# tpl = "Сума: {{ d | sum }}"
# tmpl = Template(tpl)
# msg = tmpl.render(d=digs)
# print(msg)
#
# tpl = "Максимум: {{ d | max }}"
# tmpl = Template(tpl)
# msg = tmpl.render(d=digs)
# print(msg)
#
# tpl = "Найдорожче авто: {{ d | max(attribute = 'price') }}"
# tmpl = Template(tpl)
# msg = tmpl.render(d=cars)
# print(msg)

# random
# tpl = "Случайне авто: {{ d | random }}"
# tmpl = Template(tpl)
# msg = tmpl.render(d=cars)
# print(msg)
#
# # replace
# tpl = "Нова назва авто: {{ d | replace('o', 'O') }}"    # заміна о на О
# tmpl = Template(tpl)
# msg = tmpl.render(d=cars)
# print(msg)


# Блок фільтру
# persons = [{'name':'Petro', 'age':26, 'weight':78},
#            {'name':'Ivan', 'age':36, 'weight':82},
#            {'name':'Stepan', 'age':24, 'weight':75}]

# tpl = '''
# {%- for u in users -%}
# {% filter upper%}{{u.name}}{% endfilter %}
# {% endfor -%}'''
# tmpl = Template(tpl)
# msg = tmpl.render(users=persons)
# print(msg)


# Макровизначення шаблонів
# html = '''
# {% macro input (name, value='', type=text, size=20) -%}
#     <input type='{{ type }}' name={{ name }} value={{ value|e }} size={{ size }}>
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('mail') }}
# <p>{{ input('password') }}
# '''
# tmpl = Template(html)
# msg = tmpl.render()
# print(msg)



# Вкладені макроси - call
# html = '''
# {% macro list_users(list_of_users) -%}
# <ul>
# {% for u in list_of_users -%}
#     <li>{{ u.name }}{{caller(u)}}
# {% endfor %}
# </ul>
# {%- endmacro %}
#
# {{list_users(users)}}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

persons = [{'name':'Petro', 'old':26, 'weight':78},
           {'name':'Ivan', 'old':36, 'weight':82},
           {'name':'Stepan', 'old':24, 'weight':75}]

html = '''
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{ u.name }}{{caller(u)}}
{% endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{ user.old }}
    <li>weight: {{ user.weight }}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)