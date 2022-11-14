def output_numbers_powered_to_fourth(start, end, step):
    i = start
    while i <= end:
        print(i, end="\t")
        print(i ** 4)
        i = i + step


output_numbers_powered_to_fourth(2, 14, 2)
