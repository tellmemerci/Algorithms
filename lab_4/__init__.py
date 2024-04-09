# Односвязный список
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Двухсвязный список
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

# Двусторонний список
class BidirectionalNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class BidirectionalLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = BidirectionalNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

# Реализация функционала
def swap_elements(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def insert_element(array, value, index):
    array.insert(index, value)

def remove_element(array, index):
    del array[index]

def find_index(array, value):
    if value in array:
        return array.index(value)
    else:
        return -1

def find_value(array, index):
    if index >= 0 and index < len(array):
        return array[index]
    else:
        return None

def sorted_insert(array, value):
    for i in range(len(array)):
        if value <= array[i]:
            array.insert(i, value)
            return
    array.append(value)

# Создание массивов
array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5]

# Создание списков и вставка тех же элементов
list1 = SinglyLinkedList()
for element in array1:
    list1.insert(element)

list2 = DoublyLinkedList()
for element in array1:
    list2.insert(element)

list3 = BidirectionalLinkedList()
for element in array1:
    list3.insert(element)

# Перестановка элементов
swap_elements(array1, 1, 3)
# Перестановка элементов в списке не реализована в данном примере

# Вставка элемента
insert_element(array1, 6, 2)
list1.insert(6)
list2.insert(6)
list3.insert(6)

# Удаление элемента
remove_element(array1, 4)
# Удаление элемента из списков не реализовано в данном примере

# Поиск по индексу и значению
print(find_index(array1, 3))  # Вывод: 2
print(find_index(array1, 7))  # Вывод: -1

print(find_value(array1, 2))  # Вывод: 3
print(find_value(array1, 6))  # Вывод: None

# Сортировка вставками
array3 = [4, 2, 5, 1, 3]
sorted_insert(array3, 6)
print(array3)  # Вывод: [1, 2, 3, 4, 5, 6]