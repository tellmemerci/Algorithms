import random
import time
def binary_search(list, item):
    start_time = time.perf_counter()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            end_time = time.perf_counter()
            total_time = (end_time - start_time) * 1000
            return mid, total_time
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return 'Нет данного числа в массиве'


def generation_list(size):
    list = []
    for i in range(size):
        list.append(random.randint(1, 500))
        list.sort()
    return list

def delete_element(list, element):
    start_time = time.perf_counter()
    index = 0
    while index < len(list):
        if list[index] == element:
            break
        index += 1

    if index == len(list):
        end_time = time.perf_counter()
        total_time = (end_time - start_time) * 1000
        return list, total_time

    for i in range(index, len(list) - 1):
        list[i] = list[i + 1]
    list.pop()
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000
    return list, total_time

def insert_element(list, element):
    start_time = time.perf_counter()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < element:
            low = mid + 1
        elif list[mid] > element:
            high = mid - 1
        else:
            list.insert(mid, element)
            return list
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000
    list.insert(low, element)
    return list, total_time
size = int(input('Введите размер случайного массива: '))
list = generation_list(size)
print('Ваш первоначальный массив: ', list)
digit = int(input('Введите число для поиска индекса: '))
print('Номер вашего элемента:', binary_search(list, digit))
print(list)
element = int(input('Введите число, которое хотите удалить: '))
print('Ваш массив ', delete_element(list, element))
element = int(input('Напишите число, которое хотите вставить: '))
print('Ваш массив: ', insert_element(list, element))
