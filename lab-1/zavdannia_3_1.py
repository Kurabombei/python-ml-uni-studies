import random


def get_random_elements(n):
    v = []
    for i in range(n):
        value = random.randint(1, 100)
        v.append(value)
    return v


def main():
    random_elements = get_random_elements(15)
    print("Заданий масив:", random_elements)
    print("Сума значень", sum(random_elements))


main()
