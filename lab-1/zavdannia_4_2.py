def get_length():
    return int(input("Введіть кількість елементів для масиву:\n"))


def initialize_array(number_of_elements):
    if (isinstance(number_of_elements, int)):
        temp_arr = []
        for i in range(number_of_elements):
            element = int(input("Введіть елемент №" + str(i + 1) + ": "))
            temp_arr.append(element)
        return temp_arr
    else:
        print("Кількість має бути числом")
        return []


def sort_bulbs(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
            i = i + 1
    return arr


def main():
    number_of_elements = get_length()
    array = initialize_array(number_of_elements)
    print("До сортування: ", array)
    sorted_array = sort_bulbs(array)
    print("Опісля сортування: ", sorted_array)


main()
