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


def visual(lst, flag=False):

    plt.xlim(-10.0, 10.0)
    lim = lst[-1][1]
    plt.xlabel('Элементы множеств')
    plt.ylabel('Уровни диаграммы')

    if not flag:
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
    else:
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

    plt.show()


'''
Примеры входных данных:

visual([(1, 1, []), (2, 2, [1]), (3, 3, [2]), (4, 4, [3]), (5, 5, [4]), (6, 6, [5]), (7, 7, [6]), (8, 8, [7]),
        (9, 9, [8]), (10, 10, [9]), (11, 11, [10]), (12, 12, [11])], True)
        
visual([(1, 1, []), (2, 2, [1]), (3, 3, [2]), (4, 4, [3]), (5, 5, [4]), (6, 6, [5]), (7, 7, [6])], True)

visual([(1, 1, []), (2, 2, [1]), (3, 2, [1]), (5, 2, [1]), (6, 3, [2, 3]), (10, 3, [2, 5]), (15, 3, [3, 5]), 
         (30, 4, [6, 10, 15])])
'''
