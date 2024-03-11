import random

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
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
    index = 0
    while index < len(list):
        if list[index] == element:
            break
        index += 1

    if index == len(list):
        return list

    for i in range(index, len(list) - 1):
        list[i] = list[i + 1]
    list.pop()
    return list


def insert_el(list, element):
    pass


size = int(input('Введите размер случайного массива: '))
list = generation_list(size)
print('Ваш первоначальный массив: ', list)
digit = int(input('Введите число для поиска индекса: '))
print('Номер вашего элемента:', binary_search(list, digit))
print(list)
element = int(input('Введите число, которое хотите удалить: '))
print('Ваш массив ', delete_element(list, element))
