# # Задачи на закрепление типов аргументов:
# 1.Написать функцию, которая принимает любое количество непозиционных аргументов чисел. 
# Возвращает максимальное и минимальное значение в формате tuple[0] - min, tuple[1] - max. 
def upper_or_lower(*args,case=True):
    result = ()
    for arg in args: 
        if case == True:
            arg = arg.upper()
        else:
            arg = arg.lower()
        result += arg, 
    return
upper_or_lower('Adik', 'elnur', 'MEsSI', 'ronaldo')
upper_or_lower('Adik', 'elnur', 'MEsSI', 'RONALDO', case = False)




# 2.Написать функцию, которая принимает: *args и булевое значение case по-умолчанию равный True. Если флаг действителен(true): возвращаем все args, где каждый элемент приведен к верхнему регистру, иначе - к нижнему. 
# Проверяем элементы args перед приведением регистра, что они являются строкой с помощью проверки:
# if type(arg) is str:
#    # приведение к регистру 

# 3.Написать функцию, которая принимает любое количество позиционных аргументов - строк и один параматер по-умолчанию glue. Соединить все строки. Для соединения между любых двух строк вставлять glue.


def my_func(n):
    if n == 0:
        return
    print(n)
    my_func(n-1)
my_func(5)

def my_func1(n):
    return n + (n-1)

def final(n):
    if n == 0:
        return 0
    return n + final(n-1)
final(5)
