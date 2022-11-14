def calculate_rec_area(a, b):
    return print("Площа стола розміром ширини", a, "та довжини", b, "рівна", a * b)


def get_sides():
    a = int(input('Введіть ширину: '))
    b = int(input('Введіть довжину: '))
    return a, b


def main():
    width, length = get_sides()
    # Бажана функція calculate_rec_area()
    calculate_rec_area(width, length)


main()
