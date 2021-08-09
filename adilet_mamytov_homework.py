# adilet mamytov

# 1. Среди трех чисел найти среднее
#
#    Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше #другого).

a = int(input('enter the ammount a: '))
b = int(input('enter the ammount b: '))
c = int(input('enter the ammount c: '))
numbers = [a,b,c]
maxnum=max(numbers)
minnum=min(numbers)
for num in numbers:
    if num<maxnum and num>minnum:
        print(num)

#2. Найти максимальное число из трех
#
#    Вводятся три целых числа. Определить какое из них наибольшее.

min = numbers[0]
max = numbers[0]
avarage = numbers[0]
for number in numbers:
    if number > max:
        max = number
    if number < min:
        min = number
print(max)

# print(max(numbers))