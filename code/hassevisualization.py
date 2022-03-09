import matplotlib.pyplot as plt


def dividers(num):
    return [i for i in range(int(num / 2) + 1, 0, -1) if num % i == 0]


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


def get_levels_list(lst, len_levels):
    levels_list = [[] for _ in range(len(len_levels))]
    for value in lst:
        levels_list[value[1] - 1].append(value[0])
    return levels_list


def visual(lst, flag):

    plt.xlim(-10.0, 10.0)

    plt.xlabel('Элементы множеств')
    plt.ylabel('Уровни диаграммы')

    if flag == 1:
        lim = lst[-1][1]
        len_levels = levels_length(lst)

        levels_numbers_list = get_levels_list(lst, len_levels)

        plt.ylim(-0.4, 1.2 * lim / 4)

        x_save = -10
        y_value = -0.3
        y_save = y_value

        current_level = 0

        dy = 0.3

        for level in levels_numbers_list:
            x_value = x_save
            delta = 20 / len_levels[current_level]
            delta1 = delta / 2
            x_value += delta1
            for value in level:
                plt.text(x_value, y_value, f'{value}')
                if value > 99:
                    dx = 0.5
                elif value > 9:
                    dx = 0.3
                else:
                    dx = 0.2
                plt.scatter(x_value + dx, y_value + 0.025, s=250, facecolors='none', edgecolors='black')
                x_value += delta
            y_value += dy
            current_level += 1

        y_value = y_save + dy
        for level, values in enumerate(levels_numbers_list[1:]):
            level += 1
            x_value = x_save
            delta = 20 / len_levels[level]
            delta1 = delta / 2
            x_value += delta1
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
                        if value % value1 == 0 and value1 in dividers_lst:
                            value1_dividers = dividers(value1)
                            dividers_lst = [val for val in dividers_lst if val not in value1_dividers + [value1]]
                            plt.plot([x_value1 + 0.3, x_value + 0.3], [y_value - y_previous + 0.08, y_value - 0.03],
                                     color='black')
                        x_value1 += delta_value1
                    y_previous += dy
                x_value += delta
            y_value += dy
    elif flag == 2:
        lim = lst[-1][1]
        plt.ylim(-0.4, 2 * lim)

        x_value = 0
        y_value = 0
        dy = 2 * lim / len(lst)

        plt.text(x_value, y_value, f'{lst[0][0]}')
        plt.scatter(x_value + 0.3, y_value + 0.1, s=250, facecolors='none', edgecolors='black')
        y_value += dy
        for value in lst[1:]:
            plt.text(x_value, y_value, f'{value[0]}')
            plt.scatter(x_value + 0.32, y_value + 0.1, s=250, facecolors='none', edgecolors='black')
            plt.plot([x_value + 0.3, x_value + 0.3], [y_value - 0.35, y_value - dy + 0.5], color='black')
            y_value += dy
    elif flag == 3 or flag == 4:
        plt.xlim(-50.0, 50.0)
        plt.ylim(-0.4, 1.2 * len(lst) / 4)
        x_save = -50
        y_value = -0.3
        dy = 0.3
        x = -1.75 if flag == 3 else 0
        plt.text(x, -0.3, f'{str(lst[0])[2:-2:]}')
        y_value += dy
        d1 = 90
        for level in lst[1:-1]:
            x_value = x_save
            delta = d1 / len(level)
            delta1 = delta / 2
            x_value += delta1
            for value in level:
                plt.text(x_value, y_value, f'{value}')
                x_value += delta
            y_value += dy

        plt.text(x, y_value, f'{str(lst[-1])[2:-2:]}')
        x_value = x_save
        delta = d1 / len(lst[-2])
        d = 1.5 if flag == 3 else 2
        x_value += delta / d
        for _ in lst[-2]:
            plt.plot([x_value, 0], [y_value-0.25, y_value-0.03], color='black')
            x_value += delta

        x_value = x_save
        delta = d1 / len(lst[1])
        x_value += delta
        for i in lst[1]:
            ddx = 0
            if len(i) < 7:
                ddx = delta / 2
            plt.plot([x_value - ddx, 0], [-0.03, -0.25], color='black')
            x_value += delta
        y_value = 0.3
        current_level = 2
        if flag == 3:
            if len(lst[-2][0]) == 2:
                for level in lst[2:-1:1]:
                    x_value = x_save
                    delta = 90 / len(level)
                    delta1 = delta / 1.5
                    x_value += delta1
                    for (subset, _) in level:
                        x_value1 = x_save
                        delta_value1 = 90 / len(lst[current_level-1])
                        delta1_value1 = delta_value1 / 1.5
                        x_value1 += delta1_value1
                        for (subset1, _) in lst[current_level-1]:
                            if subset1.intersection(subset):
                                plt.plot([x_value1 + 0.3, x_value + 0.3], [y_value - dy + 0.08, y_value - 0.03],
                                         color='black')
                            x_value1 += delta_value1
                        x_value += delta
                    y_value += dy
                    current_level += 1
        else:
            for level in lst[2:-1:1]:
                x_value = x_save
                delta = 90 / len(level)
                delta1 = delta / 1.5
                x_value += delta1
                for subset in level:
                    x_value1 = x_save
                    delta_value1 = 90 / len(lst[current_level-1])
                    delta1_value1 = delta_value1 / 1.5
                    x_value1 += delta1_value1
                    for subset1 in lst[current_level-1]:
                        if subset1.intersection(subset):
                            plt.plot([x_value1, x_value - 0.3], [y_value - dy + 0.08, y_value - 0.03], color='black')
                        x_value1 += delta_value1
                    x_value += delta
                y_value += dy
                current_level += 1

    plt.show()


def get_levels_list_sets(sets, g, flag=True):
    res = [[] for _ in range(sets[-1][1])]

    for subset in sets:
        if flag:
            res[subset[1]-1].append(subset[0])
        else:
            res[subset[1] - 1].append(subset[0][0])
    if flag:
        res.insert(0, ['(\u2205, M)'])
    else:
        res.insert(0, ['M'])
    print(res + [[g]])
    return res + [[g]]
