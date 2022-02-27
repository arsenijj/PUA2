def matrix_set_view(matrix_set, flag=None):
    if not flag:
        print('Исходное отношение: {', end='')
        print(*matrix_set, sep=', ', end='}\n')
    else:
        print('{', end='')
        print(*matrix_set, sep=', ', end='; ')


def print_factor(factor_set_res):
    print('Фактор-множество множества A по эквивалентности \u03B5: {', end='')
    factor_set_res = [list(subset) for subset in factor_set_res]
    for subset in factor_set_res[:-1:]:
        print('{', end='')
        print(*subset, sep=', ', end='}, ')
    print('{', end='')
    print(*factor_set_res[-1], sep=', ', end='}}\n')


def factor_set(matrix, size):
    classes = [[j + 1 for j, value in enumerate(matrix[i]) if value == 1]
                                                for i in range(size)]
    return set(frozenset(subset) for subset in classes)


def full_system_of_class_representatives(factor):
    res = []
    for subset in factor:
        res.append(min(subset))
    print('''Полная система представителей классов эквивалентности 
             u03B5 на множестве A: T={', end=''''')
    print(*res, sep=', ', end='}\u2282A\n')


def make_equivalent_closure(copy, size, matrix_set):

    for u in range(size):
        if copy[u][u] == 0:
            copy[u][u] = 1
        for k in range(size):
            if copy[u][k] and not copy[k][u]:
                copy[k][u] = 1
            for i in range(size):
                for j in range(size):
                    if copy[k][i] == copy[i][j] == 1 and copy[k][j] == 0:
                        copy[k][j] = 1

    return [(i + 1, j + 1) for i in range(size) for j in range(size)
            if copy[i][j] and (i + 1, j + 1) not in matrix_set], copy


def is_transitive(matrix, size):

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if matrix[k][i] == matrix[i][j] == 1 and matrix[k][j] == 0:
                    return False
    return True


def is_symmetric_or_antisymmetric(matrix, size):

    flag_symmetric = True
    flag_antisymmetric = True

    for i in range(size):
        for j in range(size):
            if not matrix[i][j] == matrix[j][i]:
                flag_symmetric = False
            if matrix[i][j] == matrix[j][i] == 1 and not i == j:
                flag_antisymmetric = False
            if not flag_symmetric and not flag_antisymmetric:
                return False, False

    return flag_symmetric, flag_antisymmetric


def is_reflexive_or_anti_reflexive(matrix, size):

    flag_reflexive = True
    flag_anti_reflexive = True

    for i in range(size):
        if matrix[i][i] == 0:
            flag_reflexive = False
        elif matrix[i][i] == 1:
            flag_anti_reflexive = False
        if not flag_reflexive and not flag_anti_reflexive:
            return False, False

    return flag_reflexive, flag_anti_reflexive


def get_data():
    print('Введите размер матрицы:')
    n = int(input())
    print(f'Введите построчно элементы матрицы (по {n})')
    m = [[int(elem) for elem in input().split()] for _ in range(n)]
    m_set = [(i + 1, j + 1) for i in range(n) for j in range(n) if m[i][j] == 1]
    return m, sorted(m_set), n


def hasse_greater_eq(nums):
    res = []
    res.append((nums[0], 1, []))
    for i, num in enumerate(nums[1:]):
        res.append((num, res[-1][1] + 1, [res[-1][0]]))
    return res


def hasse_division(dividers_num):
    hasse_list = []
    sl = {key: 1 for i, key in enumerate(dividers_num)}

    for number in dividers_num[1:]:
        for divider in dividers_num[:dividers_num.index(number)]:
            if number % divider == 0:
                sl[number] = sl[divider] + 1

    for k, v in sl.items():
        pod_res = []
        for k1, v1 in sl.items():
            if v1 + 1 == v and k % k1 == 0:
                pod_res.append(k1)
        hasse_list.append((k, v, pod_res))
    hasse_list.sort(key=lambda x: x[1])
    return hasse_list


def dividers(num, flag=False):
    result = []
    begin = 1
    if flag:
        begin = 2
    for i in range(begin, int(num / 2) + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result


def min_max_elements(lst):
    if lst[0][1] == lst[1][1]:
        print('Наименьшего элемента в данном множестве нет')
    else:
        print(f'Наименьший элемент множества: {lst[0][0]}')

    if lst[-1][1] == lst[-2][1]:
        print('Наибольшего элемента в данном множестве нет')
    else:
        print(f'Наибольший элемент множества: {lst[-1][0]}')

    print(f'Минимальные элементы множества: {lst[0][0]}, ', end='')
    minimum = lst[0][1]
    for values in lst[1:]:
        if values[1] == minimum:
            print(values[0], end=', ')
        else:
            break
    print('\n')
    print(f'Максимальные элементы множества: {lst[-1][0]}, ', end='')
    maximum = lst[-1][1]
    for values in lst[-2::-1]:
        if values[1] == maximum:
            print(values[0], end=', ')
        else:
            break
    print('\n')
    return


print('Вы хотите получить фактор-множество отношения и полную систему представителей классов? Да (1) или Нет (0)')

yes_or_no = int(input())
if yes_or_no:
    matrix, matrix_set, size = get_data()
    matrix_set_view(matrix_set)
    print('\n')
    print('Cвойства бинарного отношения:')
    flagT = True
    flagR = True
    flagS = True

    if is_transitive(matrix, size):
        print('Отношение является транзитивным')
    else:
        print('Отношение не является транзитивным')
        flagT = False

    symm, _ = is_symmetric_or_antisymmetric(matrix,size)
    if symm:
        print('Отношение является симметричным')
    else:
        print('Отношение не является симметричным')
        flagS = False

    refl, _ = is_reflexive_or_anti_reflexive(matrix, size)
    if refl:
        print('Отношение является рефлексивным')
    else:
        print('Отношение не является рефлексивным')
        flagR = False

    print('\n')
    if not flagS or not flagR or not flagT:
        print('Так как отношение не обладает свойством ', end='')
        if not flagS:
            print('симметричности', end=', ')
        if not flagT:
            print('транзитивности', end=', ')
        if not flagR:
            print('рефлексивности', end=', ')
        print('то для получения фактор-множества отношения, требуется построить эквивалентное замыкание.')

        copy = matrix
        ls, mt = make_equivalent_closure(copy, size, matrix_set)

        print('Эквивалентное замыкание бинарного отношения: ', end='')
        matrix_set_view(matrix_set, True)
        print(*ls, sep=', ', end='}\n\n')

        print('Матрица эквивалентного замыкания бинарного отношения:')
        for i in range(len(mt)):
            print(*mt[i])
        print('\n')

        factor_set_res = factor_set(matrix, size)
        print_factor(factor_set_res)
        full_system_of_class_representatives(factor_set_res)

    else:
        print('Заданное отношение является эквивалентным. Его матрица:')
        for i in range(len(matrix)):
            print(*matrix[i])
        print('\n')

        factor_set_res = factor_set(matrix, size)
        print_factor(factor_set_res)
        full_system_of_class_representatives(factor_set_res)

print('''Вы хотите получить минимальные/наименьшие и максимальные/наибольшие 
        элементы множества? Да (1) или Нет (0)''')
yes_or_no = int(input())
if yes_or_no:
    print('Выберите тип задания множества: число (1) или заданное множество (2)')
    set_type = int(input())

    print('Выберете тип порядка: <= (1) или отношение делимости (2)')
    order_type = int(input())

    if set_type == 1:
        print('Введите число')
        num = int(input())
        print('Хотите ли добавить единицу во множество? Да(1), Нет(0)')
        yes_or_no = int(input())
        sub_res = None
        if yes_or_no == 1:
            if order_type == 2:
                sub_res = dividers(num)
                res = hasse_division(sub_res)
            else:
                sub_res = [i + 1 for i in range(num)]
                res = hasse_greater_eq(sub_res)
        else:
            if order_type == 2:
                sub_res = dividers(num, True)
                res = hasse_division(sub_res)
            else:
                sub_res = [i + 2 for i in range(num - 1)]
                res = hasse_greater_eq(sub_res)
    else:
        print('Введите множество')
        num = [int(value) for value in input().split()]
        num = list(set(num))
        num.sort()

        if order_type == 2:
            res = hasse_division(num)
        elif order_type == 1:
            res = hasse_greater_eq(num)

    min_max_elements(res)
    print('Вы хотите получить диаграмму Хассе? Да(1) или Нет(0)')
    yes_or_no = int(input())
    if yes_or_no:
        import hassevisualization as hv
        if order_type == 1:
            hv.visual(res, True)
        else:
            hv.visual(res)
    print(res)

'''
Примеры входных данных:

3 
0 1 0
0 0 1
1 0 0

4
1 0 1 0 
1 1 0 0
0 0 1 0
0 1 0 1

5
1 0 1 1 0
0 1 0 1 0
1 0 1 1 0
1 1 1 1 0
0 0 0 0 1

8
0 1 1 0 0 0 0 0
1 0 1 0 0 0 0 0
0 1 1 0 0 0 0 0
0 0 0 1 1 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 1 1 1
0 0 0 0 0 1 1 0
0 0 0 0 0 1 1 1
'''
