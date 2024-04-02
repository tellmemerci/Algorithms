import random
import time

def generation_list(size):
    list = []
    for i in range(size):
        list.append(random.randint(0, 100000))
    return list

def sorted_insert(list):
    start_time = time.perf_counter()
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000
    return list, total_time

def sorted_selection(list):
    start_time = time.perf_counter()
    for i in range(0, len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000
    return list, total_time
def merge_sort(lst):
    start_time = time.perf_counter()
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000

    return lst, total_time

def quick_sort(arr):
    start_time = time.perf_counter()
    if len(arr) <= 1:
        return arr, 0
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000
    sorted_less, less_time = quick_sort(less)
    sorted_greater, greater_time = quick_sort(greater)
    return sorted_less + [pivot] + sorted_greater, total_time + less_time + greater_time

size = int(input('Введите размер случайного массива: '))
list = generation_list(size)
arr = list
print('Ваш первоначальный массив: ', list)
print('Сортировка вставками', sorted_insert(list))
print('Сортировка выбором: ', sorted_selection(list))
print('Сортировка слиянием: ', merge_sort(list))
print('Быстрая сортировка: ', quick_sort(arr))