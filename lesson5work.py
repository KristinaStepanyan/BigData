#  1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

f_obj = open('my_file.txt', 'w')
line = input('Введите текст \n')
while line:
    f_obj.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

f_obj.close()
f_obj = open('my_file.txt', 'r')
content = f_obj.readlines()
print(content)
f_obj.close()

#  2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#  количества слов в каждой строке.

my_file2 = open('my_file2.txt', 'r')
content = my_file2.read()
print(f'Содержимое файла: \n {content}')
my_file2 = open('my_file2.txt', 'r')
content = my_file2.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file2 = open('my_file2.txt', 'r')
content = my_file2.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file2 = open('my_file2.txt', 'r')
content = my_file2.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file2.close()


#  4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('workfile.txt', 'r') as file_obj:
    # content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('workfile.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

#  5.  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def my_sum():
    try:
        with open('my_file5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_number = line.split()
            print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
my_sum()

#  6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
#  лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
#  не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
#  по нему. Вывести словарь на экран.

subj = {}
with open('my_file6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')




