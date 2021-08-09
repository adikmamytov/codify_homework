# adilet mamytov

# 4 задание
# Пользователь заходит в приложение и вводит своё имя в список имён, фамилию в список фамилий, 
# #возраст в список возрастов, после заполнения вывод всей информации ТОЛЬКО О ТЕКУЩЕМ ПОЛЬЗОВАТЕЛЕ, 
# #после этого программа ждёт следующего пользователя.
#ПОДСКАЗКА 1:
#Для отслеживания пользователя используйте индекс в списке и при каждом новом пользователе #увеличивайте его на 1
#surname_list[current_user_index]
#name_list[current_user_index]
# ...

#ПОДСКАЗКА 2:
#Для того чтобы программа после заполнения продолжала работать - используйте цикл while.

names=[]
lastnames=[]
ages=[]
while(True):
    name=input('enter name: ')
    lastname=input('enter lastname: ')
    age=int(input('enter age: '))
    names.append(name)
    lastnames.append(lastname)
    ages.append(age)
    print('about you')
    print('name: '+names[-1])
    print('lastname: '+lastnames[-1])
    print('age: '+str(ages[-1])+'\n\n\n')
    print('all info')
    print('all names: '+str(names))
    print('all lastnames: '+str(lastnames))
    print('all ages: '+str(ages)+'\n\n\n')


