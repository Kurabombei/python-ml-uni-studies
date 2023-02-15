import numpy as np
import matplotlib.pyplot as plt
from pylab import *

txt_fname = 'generated_y_coords.txt'


def calculate_x(start, stop, step):
    return np.arange(start, stop, step)


def calculate_y(x_coords, phi):
    return np.sin(2 * np.pi * x_coords + phi)


def generate_and_save_x_coords(start, stop, step):
    phi = 0
    x_coords = calculate_x(start, stop, step)
    y_coords = calculate_y(x_coords, phi)

    np.savetxt(txt_fname, y_coords, delimiter='\n')
    return x_coords


def read_from_file(filename):
    y_coords = np.loadtxt(filename)
    return y_coords


def array_map(x, func):
    return np.array(list(map(func, x)))


def round_digits(value):
    return round(value, 6)


def main():
    # 1) generate file, with numbers of signal
    x_coords = generate_and_save_x_coords(10, 70, 0.02)
    y_coords = read_from_file(txt_fname)

    # 2) show it on screen

    # for value in y_coords:
    #     print(value, sep='\n')

    fig1 = plt.figure()
    first_plt = fig1.add_subplot()
    first_plt.plot(x_coords, y_coords, label='I(f) = sin(2πft+φ)', color='lightblue', linewidth=2)
    xlabel('Частота [Ггц]')
    ylabel('I(f)')
    title('Закон зміни інтенсивності')
    legend()
    # 3) find max and mins of function, show interception with osi koordinat

    y_max = np.max(y_coords)
    y_min = np.min(y_coords)
    y_max_index = np.where(y_coords == y_max)[0]
    y_min_index = np.where(y_coords == y_min)[0]

    y_zero_coords = array_map(y_coords, round_digits)  # окружив до 6 цифр після коми, для пошуку 0
    zero_indexes = where(y_zero_coords == 0)[0]

    # 4) show them))
    fig2 = plt.figure()
    second_plt = fig2.add_subplot()
    second_plt.plot(x_coords, y_coords, label='I(f) = sin(2πft+φ)', color='lightblue', linewidth=1)
    second_plt.plot(x_coords[y_max_index], y_max, label='Max Y', color='red', marker='x')
    second_plt.plot(x_coords[y_min_index], y_min, label='Min Y', color='green', marker='x')
    second_plt.plot(x_coords[zero_indexes], y_coords[zero_indexes], label='Zeroes', color='r', marker='o')
    xlabel('Частота [Ггц]')
    ylabel('I(f)')
    title('Максимальне та мінімальне значення, нулі функції')
    legend()

    # 5) show on 1 graph 2 graphs dependance of intensivnist, which are shifted right by pi/2

    shifted_y = calculate_y(x_coords, np.pi / 2)

    fig3 = plt.figure()
    third_plt = fig3.add_subplot()
    third_plt.plot(x_coords, y_coords, label='I(f) = sin(2πft)', color='lightblue', linewidth=1)
    third_plt.plot(x_coords, shifted_y, label='I(f) = sin(2πft+π/2)', color='red', linewidth=1)
    xlabel('Частота [Ггц]')
    ylabel('I(f)')
    title('Залежності інтенсивності сигналу I від частоти з фазою p/2 та без')
    legend()
    # 6) show on 1 graph 3 graphs
    shifted_y_pi_4 = calculate_y(x_coords, np.pi / 4)
    shifted_y_pi_8 = calculate_y(x_coords, np.pi / 8)

    fig4 = plt.figure()
    fourth_plt = fig4.add_subplot()
    fourth_plt.plot(x_coords, y_coords, label='I(f) = sin(2πft)', color='lightblue', linewidth=1)
    fourth_plt.plot(x_coords, shifted_y_pi_4, label='I(f) = sin(2πft+π/4)', color='red', linewidth=1)
    fourth_plt.plot(x_coords, shifted_y_pi_8, label='I(f) = sin(2πft+π/8)', color='green', linewidth=1)

    xlabel('Частота [Ггц]')
    ylabel('I(f)')
    title('Залежності інтенсивності сигналу I від частоти з різними фазами')
    legend()

    # 7) 3 кругові діаграми з кількістю від'ємних та додатних значень закону зміну інтенсивності в діапазонах
    #   7.1) 10-30 ГГц,
    #   7.1) 31-50 ГГц,
    #   7.1) 51-70 ГГц

    diapazon_input = [[10, 30], [31, 50], [51, 70]]
    calculated_x = []
    for i, diapazon_start_and_finish in enumerate(diapazon_input):
        calculated_x.append(calculate_x(diapazon_start_and_finish[0], diapazon_start_and_finish[1], 0.0002))

    calculated_y = []
    for x in calculated_x:
        calculated_y.append(calculate_y(x, 0))
        print(f'calculated y {calculated_y} for x {x}')

    positive = []
    negative = []
    for y in calculated_y:
        positive.append(size(where(y > 0)))
        negative.append(size(where(y < 0)))
        print(f'positive {positive}')
        print(f'negative {negative}')

    fig5, axes = plt.subplots(3, 2)

    N = ['10-30 ГГц', '31-50 ГГц', '51-70 ГГц']
    for i, n in enumerate(N):
        axes[i][0].plot(calculated_x[i], calculated_y[i], label='I(f) = sin(2πft+φ)', color='lightblue', linewidth=2)
        axes[i][1].pie(np.array([negative[i], positive[i]]), labels=['Negative', 'Positive'], colors=['blue', 'red'],
                       autopct='%1.1f%%')
        axes[i][1].set_title('Додатні та від\'ємні значення в ' + n, fontsize=5)

    legend()
    plt.show()

main()
