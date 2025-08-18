# В програмі, в просторі імен global задайте змінну universal_var = 0.
# ·      Створіть функцію з вкладеною функцією
# ·      У зовнішній функції задайте змінну universal_var = 1 та виведіть через print її значення (при виводі зазначайте простір імен).
# ·      У внутрішній функції задайте змінну universal_var = 2 та виведіть через print її значення (при виводі зазначайте простір імен).
# ·      Викличте зазначені функції,та виведіть через print значення universal_var з головної програми (при виводі зазначайте простір імен). Зрозуміло чому universal_var відрізняється щоразу ?
# ·      Поекспериментуйте з глобальною змінною universal_var у функціях (слідкуйте за результатами всіх 3 print), з використанням ключового слова global:
# ◦  додайте global у зовнішню функцію, поміняйте значення
# ◦  (закоментуйте global у зовнішній функції) додайте global у внутрішню функцію, поміняйте значення
# ◦  розкоментуйте global у зовнішній функції
# ◦  закоментуйте global в функціях, спробуйте universal_var +=1 у зовнішній та внутрішній функціях ? Викинуло виключення, чому ? А якщо повернути global  ?
# ·      робота з ключовим словом nonlocal:
# ◦  додайте func_var = 0 на рівні зовнішньої функції, запрінтуйте її (при виводі зазначайте простір імен).
# ◦  На рівні внутрішньої функції додайте func_var = 2 запрінтуйте її (при виводі зазначайте простір імен).
# ◦  Закоментуйте код з попереднього завдання, на рівні внутрішньої функції додайте nonlocal, виведіть значення func_var
# ◦  закоментуйте nonlocal, спробуйте операцію func_var+=1 Викинуло виключення, чому ? А якщо повернути nonlocal  ?

universal_var = 0


def func1():
    # global universal_var
    # universal_var = 1
    func_var = 0
    # global universal_var
    def func2():
        # global universal_var
        # universal_var = 2
        nonlocal func_var
        func_var = 2
        # print('universal_var (local space) = ', universal_var)
        print('func_var (local space) = ', func_var)
    func2()
    # print('universal_var (enclosed space) = ', universal_var)
    print('func_var (enclosed space) = ', func_var)

func1()

# print('global space = ', universal_var)

