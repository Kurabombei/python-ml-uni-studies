import math


def read_triangle_side_lengths():
    a = int(float(input('Введіть довжину сторони А: ')))
    b = int(float(input('Введіть довжину сторони B: ')))
    c = int(float(input('Введіть довжину сторони C: ')))
    return [a, b, c]


def calculate_p(sides):
    return sum(sides) / 2


def calculate_area(sides, p):
    return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


def main():
    sides = read_triangle_side_lengths()
    print("Введені сторони: ", sides)
    p = calculate_p(sides)
    print("P = (a+b+c) / 2 = ", p)
    result = calculate_area(sides, p)
    print("S = ", result)


main()
