class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, val):
        for i in range(len(self.heap)):
            if self.heap[i] == val:
                del self.heap[i]
                self._heapify_down(i)
                break

    def search(self, val):
        for i in range(len(self.heap)):
            if self.heap[i] == val:
                return True
        return False

    def heap_sort(self, arr):
        self.build_heap(arr)
        sorted_arr = []
        while len(arr) > 0:
            sorted_arr.append(self.extract_max(arr))
        return sorted_arr

    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(arr) // 2 - 1
        for i in range(n, -1, -1):
            self._max_heapify(arr, i, len(arr))

    def extract_max(self, arr):
        max_value = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        self._max_heapify(arr, 0, len(arr))
        return max_value

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def _max_heapify(self, arr, index, heap_size):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            self._max_heapify(arr, largest, heap_size)


heap = MaxHeap()
size = 12
for i in range(size):
    heap.insert(i)
arr = [4, 2, 9, 6, 1, 3, 8, 5, 7]
sorted_arr = heap.heap_sort(arr)
print(sorted_arr)  # Выводит: [9, 8, 7, 6, 5, 4, 3, 2, 1]

