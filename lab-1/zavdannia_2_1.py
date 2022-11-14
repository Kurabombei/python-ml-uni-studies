def get_year():
    return int(input("Введіть рік: "))


def check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    year = get_year()
    is_leap_year = check_leap_year(year)
    print("Результат:\n\tЦей рік є", "високосний" if is_leap_year else "не високосний")


main()
