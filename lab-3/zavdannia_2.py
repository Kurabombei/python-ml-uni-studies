import math
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def read_from_file(filename):
    x = []
    y = []
    with open(filename) as stops:
        vehicle_stops = stops.read()
    vehicle_stops = vehicle_stops.split('\n')

    print(f'vehicle_stops: {vehicle_stops}')

    x = [float(row.split(',')[0]) for row in vehicle_stops]
    y = [float(row.split(',')[1]) for row in vehicle_stops]

    print(f' {filename} -> x: {x}')
    print(f' {filename} -> y: {y}')
    return x, y

fig = plt.figure(figsize=(10, 6))

# читаємо значення координат зупинок з файлу
tram_4_x, tram_4_y = read_from_file('data/4_tram_stops.txt')
tram_8_x, tram_8_y = read_from_file('data/8_tram_stops.txt')
bus_4a_x, bus_4a_y = read_from_file('data/4a_stops.txt')
img = mpimg.imread('data/rayon.png')

chosen_points = []


def main():
    # завантажуємо карту
    imgplot = plt.imshow(img)
    plt.axis('off')

    tram_4_stops = plot(tram_4_x, tram_4_y, label='Маршрут трамваю 4', marker='o', linestyle=':', color='red', picker=5)
    tram_8_stops = plot(tram_8_x, tram_8_y, label='Маршрут трамваю 8', marker='o', linestyle=':', color='purple', picker=5)
    bus_4a_stops = plot(bus_4a_x, bus_4a_y, label='Маршрут буса 4а', marker='o', linestyle=':', color='cyan', picker=5)

    fig.canvas.mpl_connect('pick_event', onpick)
    plt.legend(loc="upper left")
    plt.show()


def calculate_distance_by_points(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_which_route(point_1, point_2):
    if point_1[0] in tram_4_x and point_2[0] in tram_4_x and point_1[1] in tram_4_y and point_2[1] in tram_4_y:
        print(f'Points are in route of tram #4')
        return tram_4_x, tram_4_y
    elif point_1[0] in tram_8_x and point_2[0] in tram_8_x and point_1[1] in tram_8_y and point_2[1] in tram_8_y:
        print(f'Points are in route of tram #8')
        return tram_8_x, tram_8_y
    elif point_1[0] in bus_4a_x and point_2[0] in bus_4a_x and point_1[1] in bus_4a_y and point_2[1] in bus_4a_y:
        print(f'Points are in route of bus 4a')
        return bus_4a_x, bus_4a_y
    else:
        print(f'These points are from diff routes, hello!?')
        chosen_points = []
        return [], []


def calculate_distance():
    if size(chosen_points) <= 1:
        print(f'size(chosen_points) <= 1 {size(chosen_points) <= 1 }')
        return
    p1 = chosen_points[len(chosen_points) - 2][0]
    p2 = chosen_points[len(chosen_points) - 1][0]
    route_x, route_y = find_which_route(p1, p2)
    if(size(route_x) < 1):
        print(f'size(route_x) < 1 {size(route_x) < 1}')
        return 0
    journey_start = min(route_x.index(p1[0]), route_x.index(p2[0]))
    journey_finish = max(route_x.index(p1[0]), route_x.index(p2[0]))

    dist = 0
    colored_journey_x = []
    colored_journey_y = []
    while journey_start < journey_finish - 1:
        dist += calculate_distance_by_points(route_x[journey_start], route_x[journey_start + 1], route_y[journey_start], route_y[journey_start + 1])
        colored_journey_x.append(route_x[journey_start])
        colored_journey_x.append(route_x[journey_start+1])
        colored_journey_y.append(route_y[journey_start])
        colored_journey_y.append(route_y[journey_start+1])
        journey_start += 1
    print(f'Distance calculated is {dist}')
    print(f'colored_journey_x is {colored_journey_x}')
    print(f'colored_journey_y is {colored_journey_y}')

    plt.plot(colored_journey_x, colored_journey_y, marker='x', linestyle='-', color='black', picker=6)
    plt.show()


def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    chosen_points.append(points)
    if size(chosen_points) > 1:
        calculate_distance()
        print(f'new point {points}')

main()
