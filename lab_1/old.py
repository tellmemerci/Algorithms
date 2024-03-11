import random
import time

def generation_list(size):
    list = []
    for i in range(size):
        list.append(random.randint(1, 500))
    return list

def search_index(list, number):
    start_time = time.perf_counter()
    for i in range(len(list)):
        if list[i] == number:
            end_time = time.perf_counter()
            total_time = (end_time - start_time) * 1000
            return i, total_time
    return 'Нет данного числа'

def deleted_el(lisr, element):
    if element in list:
        list.remove(element)
    return list

def deleted_ell(list, element):
    for i in range(0, len(list)):
        if list[i] == element:
            list.remove(element)

size = int(input('Введите размер случайного массива: '))
list = generation_list(size)
print('Ваш первоначальный массив: ', list)
number = int(input('Введите число для поиска: '))
print('Индекс данного числа: ', search_index(list, number))
element = int(input('Введите число, которое хотите удалить: '))
print('Ваш массив ', deleted_el(list, element))