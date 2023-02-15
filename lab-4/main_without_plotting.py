# -*- coding: utf8 -*-
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import medfilt


def saveToExcelFile(max_x, max_y, min_x, min_y, textname):
    min_and_max_x = np.concatenate([min_x, max_x])
    min_and_max_y = np.concatenate([min_y, max_y])
    df = pd.DataFrame(
        {'x': min_and_max_x, 'y': min_and_max_y, 'sum_max_y': '', 'sum_min_y': '', 'num_max_x': '', 'num_min_y': ''})

    sum_max_y = max_y.sum()
    sum_min_y = min_y.sum()
    num_max_x = size(max_y)
    num_min_y = size(min_y)

    df.loc[1, ['sum_max_y', 'sum_min_y', 'num_max_x', 'num_min_y']] = [sum_max_y, sum_min_y, num_max_x, num_min_y]

    with pd.ExcelWriter(textname) as writer:
        df.to_excel(writer, index=False)


def main():
    # 1. Відкрити та візуально відобразити дані з файлу для вашого варіанту. У заданому файлі є 4 колонки, де
    # 1 – номер виміру,
    # 2 – кут повороту з енкодера,
    # 3 – кут повороту зразка,
    # 4 – інтенсивність сигналу.
    # Необхідно показати залежність кута повороту зразка від інтесивності сигналу.
    angle, intensity = read_from_file('Variant_3.txt')
    print(f'angle: {angle[0:10]}')
    print(f'intensity: {intensity[0:10]}')

    mean_angle, mean_intensity = get_mean_pairs(angle, intensity)
    mean_angle = np.array(mean_angle).astype(float)
    mean_intensity = np.array(mean_intensity).astype(float)
    median_angle, median_intensity = get_median_pairs(angle, intensity)

    # 2. Застосувати фільтр низьких частот (для відсікання шумів в сигналі) та фільтр високих частот (для відсікання постійної складої сигналу). Праметри для ФНЧ та ФВЧ вибрати самостійно, шляхом аналізу вхідних даних. Результат фільтрування вивести в графічному вікні.

    low_threshold = -0.37
    high_threshold = -0.36

    filtered_low_angle, filtered_low_intensity = get_filtered_low_pairs(mean_angle, mean_intensity, low_threshold)
    filtered_high_angle, filtered_high_intensity = get_filtered_high_pairs(mean_angle, mean_intensity, high_threshold)

    # 3. Апроксимувати задану функцію з використанням засобів python. В одному графічному вікні вивести: вхідні дані,
    # отриманий результат апроксимації, та результат накладання двох графіків.
    x_data = np.linspace(np.min(mean_angle), np.max(mean_angle), size(mean_angle))
    y_data = mean_intensity

    degree = 4
    bigger_degree = 12
    coefficients = np.polyfit(x_data, y_data, degree)
    coefficients_new = np.polyfit(x_data, y_data, bigger_degree)

    approximation = np.polyval(coefficients, x_data)
    approximation8 = np.polyval(coefficients_new, x_data)

    fig4, (ax1, ax2) = plt.subplots(2, 2, figsize=(12, 12))
    ax1[0].plot(mean_angle, mean_intensity, label='Input data', color='red')
    ax1[0].set_title('Input data(mean pairs)')
    ax2[0].plot(x_data, approximation, label='Approximation with degree of ' + str(degree), color='lightblue')
    ax2[0].set_title('Approximation with degree ' + str(degree))
    ax2[1].plot(x_data, approximation8, label='Approximation with degree of ' + str(bigger_degree), color='blue')
    ax2[1].set_title('Approximation with degree ' + str(bigger_degree))
    ax1[1].plot(mean_angle, mean_intensity, label='Input data', color='red')
    ax1[1].plot(x_data, approximation, label='Approximation of ' + str(degree), color='lightblue')
    ax1[1].plot(x_data, approximation8, label='Approximation of ' + str(bigger_degree), color='blue')
    ax1[1].set_title('Together approximations and input data')
    title('Input data and approximation and overlay')
    ax1[0].legend()
    ax1[1].legend()
    ax2[0].legend()
    ax2[1].legend()

    # 4. Знайти кількість нулів функції (точки перетину з віссю абсцис). Відобразити їх візуально.
    # У разі, якщо інтенсивність сигналу приймає тільки додатні або від’ємні значення, необхідно відняти постійну
    # складову від сигналу аби отримати додатні та від’ємні значення, а відповідно і точки перетину їх з віссю абсцис.
    constant_to_add = 0.36
    adjusted_intensity = np.array(mean_intensity) + constant_to_add
    zero_indices = np.where(np.diff(np.sign(adjusted_intensity)))[0]
    zeros_x = np.array(mean_angle)[zero_indices]

    # 5. Знайти та візуально показати усі мінімальні та максимальні значення функції, для даних, які знаходяться по
    # обидві сторони від осі абсцис. Підрахувати та вивести їх значення у вигляді таблиці в окремому файлі.
    x = mean_angle
    y = adjusted_intensity

    non_filtered_max_all, non_filtered_min_all = find_all_max_and_mins_and_plot(x, y)

    # 6. Врахувати точки перегину функції, які помилково можуть вважатися як максимуми та мінімуми функції
    # (червоні кружечки на схематичному рисунку). Підрахувати та вивести їх значення у вигляді таблиці в окремому файлі.
    # Порівняти значення із отриманими в п.5. Проаналізувати результат.

    non_filtered_max_size, non_filtered_min_size = find_max_min_points_and_plot(x, y)

    # 7. Застосувати 2 типи різних фільтрів (вибрати самостійно) для фільтрації вхідних даних
    # для їх графічного представлення. Результат фільтрування показати графічно.

    def median_filter(data, window_size):
        return medfilt(data, window_size)

    def moving_average_filter(data, window_size):
        window = np.ones(int(window_size)) / float(window_size)
        return np.convolve(data, window, 'same')

    moving_average_y = moving_average_filter(adjusted_intensity, 9)
    median_y = median_filter(adjusted_intensity, 9)

    # 8. Порівняти кількість отриманих максимумів функції без фільтрування та з фільтруванням вхідної функції.
    max_moving_average_all_y_size, min_moving_average_all_y_size = find_all_max_and_mins_and_plot(x, moving_average_y,
                                                                                                  False)
    max_median_all_y_size, min_median_all_y_size = find_all_max_and_mins_and_plot(x, median_y, False)
    max_moving_average_y_size, min_moving_average_y_size = find_max_min_points_and_plot(x, moving_average_y, False)
    max_median_y_size, min_median_y_size = find_max_min_points_and_plot(x, median_y, False)
    print(f'Для всіх максимумів функції результати такі:\n' +
          f' \tНефільтрованих максимумів: {non_filtered_max_all}\n \tФільтрованих максимумів (ковзаюче середнє): {max_moving_average_all_y_size}, зміна на {non_filtered_max_all - max_moving_average_all_y_size} \tФільтрованих максимумів (медіанний): {max_median_all_y_size}, зміна на {non_filtered_max_all - max_median_all_y_size}')
    print(f'Для всіх мінімумів функції результати такі:\n' +
          f' \tНефільтрованих мінімумів: {non_filtered_min_all}\n \tФільтрованих мінімумів (ковзаюче середнє): {min_moving_average_all_y_size}, зміна на {non_filtered_min_all - min_moving_average_all_y_size} \tФільтрованих мінімумів (медіанний): {min_median_all_y_size}, зміна на {non_filtered_min_all - min_median_all_y_size}')

    print(f'Для окремих максимумів функції результати такі:\n' +
          f' \tНефільтрованих максимумів: {non_filtered_max_size}\n \tФільтрованих максимумів (ковзаюче середнє): {max_moving_average_y_size}, зміна на {non_filtered_max_size - max_moving_average_y_size} \tФільтрованих максимумів (медіанний): {max_median_y_size}, зміна на {non_filtered_max_size - max_median_y_size}')
    print(f'Для окремих мінімумів функції результати такі:\n' +
          f' \tНефільтрованих мінімумів: {non_filtered_min_size}\n \tФільтрованих мінімумів (ковзаюче середнє): {min_moving_average_y_size}, зміна на {non_filtered_min_size - min_moving_average_y_size} \tФільтрованих мінімумів (медіанний): {min_median_y_size}, зміна на {non_filtered_min_size - min_median_y_size}')

    plt.show()


def find_all_max_and_mins_and_plot(x, y, should_plot=True):
    max_indices = (np.diff(np.sign(np.diff(y))) < 0).nonzero()[0] + 1
    min_indices = (np.diff(np.sign(np.diff(y))) > 0).nonzero()[0] + 1
    max_x = x[max_indices]
    min_x = x[min_indices]
    max_y = y[max_indices]
    min_y = y[min_indices]
    # saveToExcelFile(max_x, max_y, min_x, min_y, 'max_min_pairs.xlsx')
    if should_plot:
        fig6 = plt.figure(figsize=(10, 6))
        plt6 = fig6.add_subplot()
        plt6.plot(x, y, label='Input data', color='blue')
        plt6.plot(max_x, max_y, 'ro', label='Maximum points for y')
        plt6.plot(min_x, min_y, 'bo', label='Minimal points for y')
        plt6.legend()
    return size(max_y), size(min_y)


def find_max_min_points_and_plot(x, y, should_plot=True):
    max_y = []
    max_x = []
    min_y = []
    min_x = []
    # Порозбивали в групи
    sign_groups = np.sign(y)
    indices = np.arange(size(y))
    groups = np.split(indices, np.where(np.diff(sign_groups) != 0)[0] + 1)
    # Шукаємо максимуми та мінімуми в групах
    for group in groups:
        if y[group[0]] >= 0:
            max_index = group[np.argmax(y[group])]
            max_y.append(y[max_index])
            max_x.append(x[max_index])
        else:
            min_index = group[np.argmin(y[group])]
            min_y.append(y[min_index])
            min_x.append(x[min_index])
    # saveToExcelFile(max_x, np.array(max_y), min_x, np.array(min_y), 'max_min_splited_pairs.xlsx')
    if should_plot:
        fig7 = plt.figure(figsize=(10, 6))
        plt7 = fig7.add_subplot()
        plt7.plot(x, y, label='Input data', color='blue')
        plt7.plot(max_x, max_y, 'ro', label='Maximum points for y')
        plt7.plot(min_x, min_y, 'bo', label='Minimal points for y')
        plt7.plot(x, np.full(size(x), 0), color='pink', label='y=0')
        plt7.legend()
    return size(max_y), size(min_y)


def get_mean_pairs(angle, intensity):
    x = np.array(angle).astype(float)
    y = np.array(intensity).astype(float)

    unique_pairs = set(zip(x, y))

    mean_y_dict = {}
    for pair in unique_pairs:
        if pair[0] not in mean_y_dict:
            mean_y_dict[pair[0]] = [pair[1]]
        else:
            mean_y_dict[pair[0]].append(pair[1])

    mean_y = [np.nanmean(mean_y_dict[x_val]) for x_val in sorted(mean_y_dict.keys())]

    return list(sorted(mean_y_dict.keys())), mean_y


def get_median_pairs(angle, intensity):
    x = np.array(angle).astype(float)
    y = np.array(intensity).astype(float)

    unique_pairs = set(zip(x, y))

    median_y_dict = {}
    for pair in unique_pairs:
        if pair[0] not in median_y_dict:
            median_y_dict[pair[0]] = [pair[1]]
        else:
            median_y_dict[pair[0]].append(pair[1])

    median_y = [np.median(median_y_dict[x_val]) for x_val in sorted(median_y_dict.keys())]

    return list(sorted(median_y_dict.keys())), median_y


def get_filtered_low_pairs(mean_angle, mean_intensity, threshold):
    x = np.array(mean_angle).astype(float)
    y = np.array(mean_intensity).astype(float)
    indexes = np.where(y < threshold)
    return x[indexes], y[indexes]


def get_filtered_high_pairs(mean_angle, mean_intensity, threshold):
    x = np.array(mean_angle).astype(float)
    y = np.array(mean_intensity).astype(float)
    indexes = np.where(y >= threshold)
    return x[indexes], y[indexes]


def read_from_file(filename):
    with open(filename) as all_data:
        estimations = all_data.read()
    estimations = estimations.split('\n')
    angle_example = [row.split('\t')[2] for row in estimations]
    intensity_sygnal = [row.split('\t')[3] for row in estimations]
    return angle_example, intensity_sygnal


main()
