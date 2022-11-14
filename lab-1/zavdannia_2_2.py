def check_number(number):
    if number < 0:
        return "Введіть додатне число"
    else:
        if number >= 0 and number < 10:
            return "Введіть число більше 10"
        else:
            return "Ви ввели число " + str(number)


def get_number():
    return int(input("Введіть число від 10 до 100: "))


def main():
    number = get_number()
    print(check_number(number))


main()
