# 1 задание
# Дан список [5,4,3,2,1,3,4,5,6,7,8,9,0], используя ключевое слово del - сформируйте новый: [2]

my_list = [5,4,3,2,1,3,4,5,6,7,8,9,0]
del my_list[0] 
del my_list[0]
del my_list[0]
del my_list[1]
del my_list[1]
del my_list[1]
del my_list[1]
del my_list[1]
del my_list[1]
del my_list[1]
del my_list[1]
del my_list[1]
print (my_list)

# 2 задание
# Дан список [5,4,3,2,1,3,4,5,6,7,8,9,0], используя ключевое слово append, insert - сформируйте новый: [5,4,3,2,1,3,4,'new element 0',6,7,8,9,0,'new element 1','new element 2']
next_list = [5,4,3,2,1,3,4,5,6,7,8,9,0]
next_list.append('new element 1')
next_list.append('new element 2')
next_list.insert(7,'new element 0')
del next_list [8]
print(next_list)


# 3 задание
# Дан список [1,2,3,[88.99,33], 4], используя append, insert, замещение по индексу, ключевое #слово del # - сформируйте новый:
# [2,1,33, ['test'], 4, 97, 55, 34, 12]
one_list = [1,2,3,[88.99,33], 4]
one_list[0] = 2
one_list[1] = 1
one_list[2] = 33
del one_list[3]
one_list.insert(3, ['test'])
one_list.append(97)
one_list.append(55)
one_list.append(34)
one_list.append(12)
print(one_list)



# 4 задание
# Пользователь заходит в приложение и вводит своё имя в список имён, фамилию в список фамилий, #возраст в список возрастов, после заполнения вывод всей информации ТОЛЬКО О ТЕКУЩЕМ ПОЛЬЗОВАТЕЛЕ, #после этого программа ждёт следующего пользователя.
#ПОДСКАЗКА 1:
#Для отслеживания пользователя используйте индекс в списке и при каждом новом пользователе #увеличивайте его на 1
#surname_list[current_user_index]
#name_list[current_user_index]
# ...

#ПОДСКАЗКА 2:
#Для того чтобы программа после заполнения продолжала работать - используйте цикл while.

name_list =[]
surname_list = []
age_list = []
current_user_index = 0
action = None
# while != 'exit'
name = input('enter the name: ')
surname = input('enter the surname: ')
age = input('enter the age: ')
name_list.append(name)
surname_list.append(surname)
age_list.append(age)
print("name: {0}".format(name_list[current_user_index]))
current_user_index += 1
# ask user to enter action 

