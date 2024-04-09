import time

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size

    def hash_function1(self, key):
        return len(key) % self.table_size

    def hash_function2(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum % self.table_size

    def insert(self, key, value):
        start_time = time.perf_counter()

        index = self.hash_function1(key)
        probes = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                print(f"Insert Execution Time: {execution_time}")
                return
            else:
                probes += 1
                index = (self.hash_function1(key) + self.probing_function(probes)) % self.table_size
                if probes == self.table_size:
                    raise ValueError("Table is full.")
        self.table[index] = (key, value)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Insert Execution Time: {execution_time}")

    def delete(self, key):
        start_time = time.perf_counter()

        index = self.hash_function1(key)
        probes = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                print(f"Delete Execution Time: {execution_time}")
                return
            else:
                probes += 1
                index = (self.hash_function1(key) + self.probing_function(probes)) % self.table_size
                if probes == self.table_size:
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    print(f"Delete Execution Time: {execution_time}")
                    return

    def search(self, key):
        start_time = time.perf_counter()

        index = self.hash_function1(key)
        probes = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                print(f"Search Execution Time: {execution_time}")
                return self.table[index][1]
            else:
                probes += 1
                index = (self.hash_function1(key) + self.probing_function(probes)) % self.table_size
                if probes == self.table_size:
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    print(f"Search Execution Time: {execution_time}")
                    return None

    def probing_function(self, probes):
        return probes**2  # Квадратичное пробирование

def show_hash_table(hash_table):
    for index, item in enumerate(hash_table.table):
        if item is not None:
            print(f"Index {index}: {item[0]} - {item[1]}")
        else:
            print(f"Index {index}: None")

table_size = int(input('Введите размер хэш-таблицы: '))
hash_table = HashTable(table_size)
hash_table.insert("Александр", 89990000001)
hash_table.insert("Алексей", 89990000002)

hash_table.insert("Андрей", 89990000003)
print('Хэш-таблица')
show_hash_table(hash_table)
key = input('Введите имя пользователя: ')
value = input('Введите номер телефона: ')
hash_table.insert(key, value)
show_hash_table(hash_table)
name = input('Напишите имя для поиска: ')
search_result = hash_table.search(name)
print(f"Search Result: {search_result}")
name = input('Напишите имя для удаления: ')
hash_table.delete(name)
show_hash_table(hash_table)

print('Проверка того, что пользователь удален. Если будет None - пользователь удален')
key = input('Введите имя пользователя: ')
search_result = hash_table.search(key)
print(f"Search Result: {search_result}")
