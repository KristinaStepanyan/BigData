# 1.Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['Kristina', 'hello' , 21 , 165.6, {'name', 'surname', 'age'}, (3, 5, 'Moscow')]
print(my_list)
for types in my_list:
    print(f'{types} is {type(types)}')

# 2.Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

second_list = []
n = int(input('Количество элементов в списке:'))  # количество элементов в списке
for i in range(n):
    print('Введите новый элемент:')
    new_element = input()
    second_list.append(new_element)

print(second_list)
if len(second_list) % 2 == 0:
    p = 0   # значение идекса
    while p < len(second_list):
        element = second_list[p]
        second_list[p] = second_list[p+1]
        second_list[p+1] = element
        p += 2
else:
    p = 0
    while p < len(second_list) - 1:
        element = second_list[p]
        second_list[p] = second_list[p + 1]
        second_list[p + 1] = element
        p += 2
print(second_list)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

calendar_dict = {1: 'Зима' , 2: 'Весна', 3: 'Лето', 4: 'Осень'}
calendar_list = ['Зима', 'Весна', 'Лето', 'Осень']
number = int(input('Введите номер месяца от 1 до 12:'))
if number == 1 or number == 2 or number == 12:
    print(calendar_dict.get(1))
    print(calendar_list[0])
elif number == 3 or number == 4 or number == 5:
    print(calendar_dict.get(2))
    print(calendar_list[1])
elif number == 6 or number == 7 or number == 8:
    print(calendar_dict.get(3))
    print(calendar_list[2])
elif number == 9 or number == 10 or number == 11:
    print(calendar_dict.get(4))
    print(calendar_list[3])
else:
    print('Такого месяца нет.')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input('Введите строку:')
k = my_str.split(' ')
for i, el in enumerate(k, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")























