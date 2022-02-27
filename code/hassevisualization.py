import matplotlib.pyplot as plt


def dividers(num):
    return [(i, False) for i in range(int(num / 2) + 1, 0, -1) if num % i == 0]


def levels_length(lst):
    max_len = 1
    max_level_length_list = []
    value = lst[0][1]
    for values in lst[1:]:
        if values[1] == value:
            max_len += 1
        if values[1] != value:
            max_level_length_list.append(max_len)
            max_len = 1
            value = values[1]

    max_level_length_list.append(max_len)
    return max_level_length_list


def visual(lst, flag=False):
    plt.xlim(-10.0, 10.0)
    lim = lst[-1][1]
    plt.xlabel('Элементы множеств')
    plt.ylabel('Уровни диаграммы')

    if not flag:
        len_levels = levels_length(lst)

        levels_numbers_list = [[] for _ in range(len(len_levels))]
        for value in lst:
            levels_numbers_list[value[1] - 1].append(value[0])
        plt.ylim(-0.4, 1.2 * lim / 4)

        x = -10
        x_save = -10

        y = -0.3
        y_save = y

        current_level = 0

        delta = 20 / len_levels[current_level]
        delta1 = delta / 2
        x += delta1

        dy = 0.3
        dx = 0.2
        plt.text(x, y, f'{lst[0][0]}')
        plt.scatter(x + 0.2, y + 0.025, s=250, facecolors='none', edgecolors='black')
        x += delta
        for i, value in enumerate(lst[1:]):
            if lst[i+1][1] == lst[i][1]:

                plt.text(x, y, f'{value[0]}')

                if value[0] > 9:
                    dx = 0.3
                if value[0] > 99:
                    dx = 0.5
                plt.scatter(x + dx, y + 0.025, s=250, facecolors='none', edgecolors='black')

                dx = 0.2
                x += delta

            if lst[i][1] != lst[i+1][1]:
                current_level += 1
                x = x_save
                delta = 20 / len_levels[current_level]
                delta1 = delta / 2
                x += delta1
                y += dy
                if value[0] > 9:
                    dx = 0.3
                if value[0] > 99:
                    dx = 0.5

                plt.text(x, y, f'{value[0]}')
                plt.scatter(x + dx, y + 0.025, s=250, facecolors='none', edgecolors='black')
                dx = 0.2
                x += delta

        y = y_save + dy
        for level, values in enumerate(levels_numbers_list[1:]):
            level += 1
            x = x_save
            delta = 20 / len_levels[level]
            delta1 = delta / 2
            x += delta1
            current_level = level
            for value in values:
                dividers_lst = dividers(value)
                y_previous = dy
                for i, values_levels in enumerate(levels_numbers_list[level - 1::-1]):
                    x_value1 = x_save
                    delta_value1 = 20 / len_levels[current_level - i - 1]
                    delta1_value1 = delta_value1 / 2
                    x_value1 += delta1_value1
                    for value1 in values_levels:
                        if value % value1 == 0 and (value1, False) in dividers_lst:
                            dividers_lst.remove((value1, False))
                            for val in dividers(value1):
                                if val in dividers_lst:
                                    dividers_lst.remove(val)
                            plt.plot([x_value1 + 0.3, x + 0.3], [y - y_previous + 0.08, y - 0.03], color='black')
                        x_value1 += delta_value1
                    y_previous += dy
                x += delta
            y += dy
    else:
        plt.ylim(-0.4, 2 * lim)

        x = 0
        y = 0
        dy = 2 * lim / len(lst)

        plt.text(x, y, f'{lst[0][0]}')
        plt.scatter(x + 0.3, y + 0.1, s=250, facecolors='none', edgecolors='black')
        y += dy
        for value in lst[1:]:
            plt.text(x, y, f'{value[0]}')
            plt.scatter(x + 0.32, y + 0.1, s=250, facecolors='none', edgecolors='black')
            plt.plot([x + 0.3, x + 0.3], [y - 0.35, y - dy + 0.5], color='black')
            y += dy

    plt.show()


'''
visual([(1, 1, []), (2, 2, [1]), (3, 3, [2]), (4, 4, [3]), (5, 5, [4]), (6, 6, [5]), (7, 7, [6]), (8, 8, [7]),
        (9, 9, [8]), (10, 10, [9]), (11, 11, [10]), (12, 12, [11])], True)
        
visual([(1, 1, []), (2, 2, [1]), (3, 3, [2]), (4, 4, [3]), (5, 5, [4]), (6, 6, [5]), (7, 7, [6])], True)

visual([(2, 1, []), (3, 1, []), (4, 2, [2]), (14, 2, [2]), (15, 2, [3]), (21, 2, [3]), (8, 3, [4]), (30, 3, [15]),
        (16, 4, [8]), (32, 5, [16])])
'''