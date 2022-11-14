import random


def get_random_elements(n):
    v = []
    for i in range(n):
        value = random.randint(1, 100)
        v.append(value)
    return v


def heapify(arr, arr_len, i):
    # ініціалізація найбільшого нода як i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # якщо лівий чайлд нод існує і більший за батьківський
    if left < arr_len and arr[largest] < arr[left]:
        largest = left
    # якщо правий чайлд нод існує і більший за батьківський
    if right < arr_len and arr[largest] < arr[right]:
        largest = right
    # замінюємо основу (root) якщо найбільший нод був змінений (не початковий i)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # рекурсивний виклик функції
        heapify(arr, arr_len, largest)


def heap_sort(arr):
    arr_len = len(arr)

    # побудова купи (building heap)
    for i in range(arr_len // 2 - 1, -1, -1):
        heapify(arr, arr_len, i)
    # видалення елементу (extracting element), а по типу заміна першого і і-того елементу,
    # що розділяє масив на посортовану і не посортовану області
    for i in range(arr_len - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def main():
    random_elements = get_random_elements(50)
    print("Заданий масив:", random_elements)
    sorted_elements = heap_sort(random_elements)
    print("Посортований масив", sorted_elements)


main()