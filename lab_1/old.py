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

def deleted_el(list, element):
    start_time = time.perf_counter()
    if element in list:
        list.remove(element)
        end_time = time.perf_counter()
        total_time = (end_time - start_time) * 1000
    return list, total_time

def deleted_ell(list, element):
    start_time = time.perf_counter()
    for i in range(0, len(list)):
        if list[i] == element:
            list.remove(element)
            end_time = time.perf_counter()
            total_time = (end_time - start_time) * 1000
            return list, total_time

def insert_element(lst, element):
    start_time = time.perf_counter()
    lst.append(element)
    lst.sort()
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000
    return lst, total_time



size = int(input('Введите размер случайного массива: '))
list = generation_list(size)
print('Ваш первоначальный массив: ', list)
number = int(input('Введите число для поиска: '))
print('Индекс данного числа: ', search_index(list, number))
element = int(input('Введите число, которое хотите удалить: '))
print('Ваш массив ', deleted_el(list, element))
element = int(input('Введите число, которое хотите вставить: '))
print('Ваш массив: ', insert_element(list, element))