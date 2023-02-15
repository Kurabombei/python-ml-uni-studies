

def calc_regression(coords_x, coords_y):
    x = coords_x.tolist()
    y = coords_y.tolist()
    x2 = []
    y2 = []
    xy = []
    for i in range(len(x)):
        xx = x[i] * x[i]
        x2.append(xx)
        yy = y[i] * y[i]
        y2.append(yy)
        xy2 = x[i] * y[i]
        xy.append(xy2)

    # calculate sums
    sum_x = sum(x)
    x.append(sum_x)
    sum_y = sum(y)
    y.append(sum_y)
    sum_x2 = sum(x2)
    x2.append(sum_x2)
    sum_y2 = sum(y2)
    y2.append(sum_y2)
    sum_xy = sum(xy)
    xy.append(sum_xy)

    # koeficients
    a = np.array([[sum_x2, sum_x], [sum_x, len(x) - 1]])
    print(f'a: {a}')
    b = np.array([sum_xy, sum_y])
    y_new = np.linalg.solve(a, b)
    print(f'y_new: {y_new}')
    print(f'Р-ня регресійної залежності -> {y_new[0]}*x + {y_new[1]}')
    data = x * y_new[0] + y_new[1]
    print(f'data: {data}')

    # correlation
    corr = (len(x) * sum_xy - sum_x * sum_y) / math.sqrt((len(x) * sum_x2 - sum_y * sum_y))
    print(f'corr: {corr}')
    return data
