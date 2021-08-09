# adilet mamytov
# Дан кортеж (1, '2', 3, 4, '5', 6, 7, '8') сформируйте новый без строк с помощью цикла for и проверки на int:
# type(i) == int, где i - новый элемент в цикле


my_tuple = (1, '2', 3, 4, '5', 6, 7, '8')
temp_tuple=[]

for i in my_tuple:
    if type(i)==int:
        temp_tuple.append(i)

new_tuple=tuple(temp_tuple)

print(new_tuple)